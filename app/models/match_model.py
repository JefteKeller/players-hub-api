from sqlalchemy.orm import backref
from werkzeug.security import generate_password_hash, check_password_hash

from . import db


class MatchModel(db.Model):
    __tablename__ = "matches"

    id = db.Column(db.Integer, primary_key=True)
    match_winner = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)

    game_id = db.Column(db.Integer, db.ForeignKey("games.id"))
    game = db.relationship(
        "GameModel",
        uselist=False,
        lazy="joined",
        backref=db.backref(
            "match",
            lazy="joined",
        ),
    )
