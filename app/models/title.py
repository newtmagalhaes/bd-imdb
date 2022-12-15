from ..db import db

class Title(db.Model):
    __tablename__ = 'Titulos'

    title_id = db.Column(db.Integer, primary_key=True, nullable=False)
    ordering = db.Column(db.Integer, primary_key=True)
    title_name = db.Column(db.String(128), nullable=False)
    region = db.Column(db.String(128), nullable=False)
    types = db.Column(db.String(128))
    attributes = db.Column(db.String(128))
    is_original_title = db.Column(db.Boolean, default=False, nullable=False)
