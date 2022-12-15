from app.models import db


class Rating(db.Model):
    __tablename__ = "ratings"

    rating_id=db.Column(db.Integer, primary_key=True)
    averageRating=db.Column(db.Integer(128), nullable=False)
    numVotes=db.Column(db.Integer(128), nullable=False)
