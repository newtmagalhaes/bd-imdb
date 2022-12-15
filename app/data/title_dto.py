from flask_restx import Namespace, fields

class TitleDTO:
    api = Namespace('Títulos')
    titulo = api.model(
        'título',
        {
            "title_id": fields.String(description='id de um título'),
            "ordering": fields.String(description='id para unicamente identificar linhas de um mesmo title_id'),
            "title_name": fields.String(description='Nome do título'),
            "region": fields.String(description='Região do título'),
            "language": fields.String(description='Idioma do título'),
            "types": fields.List(fields.String, description='Meios de distribuição'),
            "attributes": fields.String(description='termos adicionais'),
            "is_original_title": fields.Boolean(description='Verdadeiro se é o título original'),
        }
    )