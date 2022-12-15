from flask_restx import Resource

from ..data.rating_dto import RatingDTO
from ..service.rating_service import get_all_ratings

api = RatingDTO.api
rating = RatingDTO.rating

@api.route('/')
class Rating(Resource):
    @api.doc("Retorna todos as avaliações do banco")
    @api.marshal_list_with(rating)
    def get(self) -> 'tuple[list[Rating], int]':
        return get_all_ratings(), 200
