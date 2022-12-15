from app.db import db


class Film(db.Model):
    __tablename__ = "films"

    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.Integer(40), nullable=False)
    year=db.Column(db.Integer(4), nullable=False)
    language=db.Column(db.Integer(20), nullable=False)
    producer_id=db.Column(db.Integer, db.ForeignKey('producer.id'), unique=True)
    producer=db.relationship("Producer", backref=db.backref("parent", uselist=False))