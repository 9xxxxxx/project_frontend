from flask import Blueprint, jsonify, request
from app.db import MySQLPool
from contextlib import closing
import logging

bp_data = Blueprint("getdata", __name__, url_prefix="/api/getdata")

@bp_data.route("/", methods=["GET"])
def getdata():
    try:
        # 获取查询参数
        rows = request.args.get("rows", default=50, type=int)
        offset = request.args.get("offset", default=0, type=int)
        start_date = request.args.get("start_date", default=None)
        end_date = request.args.get("end_date", default=None)
        search = request.args.get("search", default=None)

        conditions = []
        params = []

        # 日期范围过滤
        if start_date:
            conditions.append("日期 >= %s")
            params.append(start_date)
            
        if end_date:
            conditions.append("日期 <= %s")
            params.append(end_date)

        # 模糊搜索（假设有“产品名称”字段）
        if search:
            conditions.append("产品名称 LIKE %s")
            params.append(f"%{search}%")

        where_clause = f"WHERE {' AND '.join(conditions)}" if conditions else ""

        # 构建 SQL
        sql = f"""
            SELECT DATE_FORMAT(日期, '%Y-%m-%d') AS 日期,
                   标准人力,
                   标准工时,
                   标准产量 
            FROM motor
            {where_clause}
            ORDER BY 日期 DESC
            LIMIT %s OFFSET %s
        """
        params.extend([rows, offset])

        with closing(MySQLPool.get_connection()) as conn:
            with closing(conn.cursor(dictionary=True)) as cursor:
                cursor.execute(sql, tuple(params))
                data = cursor.fetchall()

                response = jsonify(data)
                response.headers["Content-Type"] = "application/json; charset=utf-8"
                return response

    except Exception as e:
        logging.error(f"API Error: {str(e)}")
        return jsonify({"success": False, "error": "Internal Server Error"}), 500
