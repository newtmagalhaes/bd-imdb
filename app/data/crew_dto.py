from flask_restx import Namespace, fields

class CrewDTO:
    api = Namespace('Crews')
    crew = api.model(
        'crew',
        {
            "crew_id": fields.String(description='Crew id'),
            "directors": fields.String(description='Diretores'),
            "writers": fields.String(description='Escritores'),
        }
    )