from ..models.film import Film


def get_all_films() -> 'list[Film]':
    return Film.query.all()
