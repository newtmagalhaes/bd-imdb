from flask import Flask
from werkzeug.exceptions import HTTPException

from .db import db, init_db, load_tsv_into_db
from .routes import blueprint


def create_app() -> Flask:
    """Fabrica de Aplicação Flask"""
    app = Flask(__name__)

    # Setup api endpoints
    app.register_blueprint(blueprint)

    # Setup database
    init_db(app)

    @app.before_first_request
    def restart_db():
        db.drop_all()
        db.create_all()
        # load_tsv_into_db()
        db.session.commit()

    # Global Exception Error
    @app.errorhandler(Exception)
    def handle_exception(error) -> 'tuple[dict[str, dict[str, str]], int]':
        print(error)
        status_code = error.code if isinstance(error, HTTPException) else 200
        return {'error': {'message': str(error)}}, status_code
    
    return app
