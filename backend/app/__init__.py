# backend/app/__init__.py
from flask import Flask
from sqlmodel import SQLModel
from app.db import engine
from app.views.user import bp_user
from app.views.getdata import bp_data



def create_app():
    app = Flask(__name__)
    app.config.update({
    'MYSQL_HOST': 'localhost',
    'MYSQL_PORT': 3306,
    'MYSQL_USER': 'root',
    'MYSQL_PASSWORD': '000000',
    'MYSQL_DB': 'stone_bi'
    })
    # SQLModel.metadata.create_all(engine)
    app.register_blueprint(bp_user) 
    app.register_blueprint(bp_data) 
    return app
