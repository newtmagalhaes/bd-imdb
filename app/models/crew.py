
from app.models import db

class Crew(db.Model):
    __tablename__ = "crew"

    id=db.Column(db.Integer,primary_key=True)
    ordering=db.Column(db.String(80), unique=True, nullable=False)
    title_name=db.Column(db.String(80), nullable=False)
    region=db.Column(db.String(80), nullable=False)
    language =db.Column(db.String(80), nullable=False)
    types=db.Column(db.String(80), nullable=False)
    attributes=db.Column(db.String(80), nullable=False)
    is_original_title=db.Column(db.Boolean(80), nullable=False)
