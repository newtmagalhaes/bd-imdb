from ..models.title import Title


def get_all_titles() -> 'list[Title]':
    return Title.query.all()
