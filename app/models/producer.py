from app.db import db


class Producer(db.Model):
    __tablename__ = "producers"

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Integer(40), nullable=False)
    phone=db.Column(db.Integer(40), nullable=False)