import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLITE_FILE_NAME = "flask_app.db"
SQLITE_FILE_PATH = f"sqlite:///{os.path.join(BASE_DIR, SQLITE_FILE_NAME)}"

db = SQLAlchemy()

def init_db(app: Flask):
    with app.app_context():
        app.config["SQLALCHEMY_DATABASE_URI"] = SQLITE_FILE_PATH
        db.init_app(app)
