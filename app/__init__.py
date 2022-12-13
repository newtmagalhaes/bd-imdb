from os import listdir
from os.path import isfile, join

import pandas as pd
from flask import Flask, render_template

from .db import BASE_DIR, db, init_db


def create_app() -> Flask:
    """Fabrica de Aplicação Flask"""
    app = Flask(__name__)

    # Setup database
    init_db(app)

    @app.route('/')
    def index():
        return render_template('base.html')
    
    @app.cli.command('create_db')
    def create_db():
        db.drop_all()
        # db.create_all()

        file_names = [f for f in listdir('./data/') if isfile(join(BASE_DIR, f))]
        table_names = range(len(file_names)) # mudar para nome dos models
        for table, file in zip(table_names, file_names):
            pd.read_table(f'./data/{file}') \
                .to_sql(name=table, con=db.engine, if_exists='replace')

        db.session.commit()

    return app
