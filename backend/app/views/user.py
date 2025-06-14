# backend/app/views/user.py
from flask import Blueprint, request, jsonify
from sqlmodel import select
from app.models.main import User
from app.db import get_session

bp_user = Blueprint("user", __name__, url_prefix="/api/users")

@bp_user.route("/", methods=["GET"])
def list_users():
    with get_session() as session:
        users = session.exec(select(User)).all()
        return jsonify([u.model_dump() for u in users])

@bp_user.route("/", methods=["POST"])
def create_user():
    data = request.json
    user = User(**data)
    with get_session() as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return jsonify(user.model_dump()), 201
        