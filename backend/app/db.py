from sqlmodel import create_engine, Session
import mysql.connector.pooling
from flask import current_app


DATABASE_URL = "mysql+mysqlconnector://root:000000@localhost:3306/stone_bi?charset=utf8mb4"
engine = create_engine(DATABASE_URL, echo=True)

DATABASE_URL2 = "mysql+mysqlconnector://root:000000@localhost:3306/test?charset=utf8mb4"
new_engine = create_engine(DATABASE_URL2, echo=True)

def get_session():
    return Session(engine)

def getdata_session():
    return Session(new_engine)

class MySQLPool:
    __pool = None

    @classmethod
    def get_pool(cls):
        """获取连接池（单例模式）"""
        if cls.__pool is None:
            cls.__pool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name="flask_pool",
                pool_size=5,  # 连接池大小
                pool_reset_session=True,
                host=current_app.config['MYSQL_HOST'],
                port=current_app.config['MYSQL_PORT'],
                user=current_app.config['MYSQL_USER'],
                password=current_app.config['MYSQL_PASSWORD'],
                database=current_app.config['MYSQL_DB'],
                charset='utf8mb4'
            )
        return cls.__pool

    @classmethod
    def get_connection(cls):
        """从连接池获取连接"""
        return cls.get_pool().get_connection()
