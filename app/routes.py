from flask import Blueprint
from flask_restx import Api

from .controller.title_controller import api as title_ns
from .default_exception import DefaultException

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint,
    title="API",
    version="1.0",
    description="API",
    security="apikey"
)

api.add_namespace(title_ns, path='/title')

api.errorhandler(DefaultException)
