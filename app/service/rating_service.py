from ..models.rating import Rating


def get_all_ratings() -> 'list[Rating]':
    return Rating.query.all()
