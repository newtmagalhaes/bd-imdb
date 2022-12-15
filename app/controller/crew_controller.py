from flask_restx import Resource

from ..data.crew_dto import CrewDTO
from ..service.crew_service import get_all_crews

api = CrewDTO.api
crew = CrewDTO.crew

@api.route('/')
class Crew(Resource):
    @api.doc("Retorna todos os crews do banco")
    @api.marshal_list_with(crew)
    def get(self) -> 'tuple[list[Crew], int]':
        return get_all_crews(), 200
