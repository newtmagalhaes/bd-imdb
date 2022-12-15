from ..models.crew import Crew


def get_all_crews() -> 'list[Crew]':
    return Crew.query.all()
