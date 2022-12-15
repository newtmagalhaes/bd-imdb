from app.models import db


class Crew(db.Model):
    __tablename__ = "crews"

    crew_id=db.Column(db.Integer, primary_key=True)
    directors=db.Column(db.String(128), nullable=False)
    writers=db.Column(db.String(128), nullable=False)
