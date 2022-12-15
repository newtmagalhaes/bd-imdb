from app.db import db


class Review(db.Model):
    __tablename__ = "reviews"

    id=db.Column(db.Integer, primary_key=True)
    stars=db.Column(db.Integer, nullable=False)