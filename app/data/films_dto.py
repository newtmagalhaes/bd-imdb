from flask_restx import Namespace, fields

class FilmsDTO:
    api = Namespace('Films')
    film = api.model(
        'film',
        {
            "id": fields.String(description='id de um título'),
        }
    )