from flask_restx import Resource

from ..data.title_dto import TitleDTO
from ..service.title_service import get_all_titles

api = TitleDTO.api
titulo = TitleDTO.titulo

@api.route('/')
class Title(Resource):
    @api.doc("Retorna todos os títulos do banco")
    @api.marshal_list_with(titulo)
    def get(self) -> 'tuple[list[Title], int]':
        return get_all_titles(), 200
