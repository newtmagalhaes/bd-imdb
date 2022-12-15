from flask_restx import Resource

from ..data.films_dto import FilmsDTO
from ..service.film_service import get_all_films

api = FilmsDTO.api
film = FilmsDTO.titulo

# Somente Get
# Post será manual
@api.route('/')
class Film(Resource):
    @api.doc("Retorna todos os títulos do banco")
    @api.marshal_list_with(film)
    def get(self) -> 'tuple[list[Film], int]':
        return get_all_films(), 200

