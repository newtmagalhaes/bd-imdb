from os import listdir, path

import pandas as pd
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

BASE_DIR = path.abspath(path.dirname(__file__))
SQLITE_FILE_NAME = "flask_app.db"
SQLITE_FILE_PATH = f"sqlite:///{path.join(BASE_DIR, SQLITE_FILE_NAME)}"

db = SQLAlchemy()

def init_db(app: Flask):
    with app.app_context():
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/mydb"
        db.init_app(app)

# TODO function
def load_tsv_into_db():
    file_names = [f for f in listdir('./datasets/') if path.isfile(path.join(BASE_DIR, f))]
    table_names = range(len(file_names)) # mudar para nome dos models
    for table, file in zip(table_names, file_names):
        pd.read_table(f'./datasets/{file}') \
            .to_sql(name=table, con=db.engine, if_exists='replace')
