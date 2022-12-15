from flask_restx import Namespace, fields

class RatingDTO:
    api = Namespace('Ratings')
    rating = api.model(
        'rating',
        {
            "rating_id": fields.String(description='Rating id'),
            "averageRating": fields.String(description='Média das avaliações'),
            "numVotes": fields.String(description='Quantidade de votos'),
        }
    )