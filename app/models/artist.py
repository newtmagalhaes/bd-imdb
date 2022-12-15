from app.db import db


class Artist(db.Model):
    __tablename__ = "artists"

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Integer(40), nullable=False)
    gender=db.Column(db.Integer(20), nullable=False)