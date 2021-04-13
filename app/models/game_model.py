from sqlalchemy.orm import backref
from werkzeug.security import generate_password_hash, check_password_hash

from . import db


class GameModel(db.Model):
    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True)
    game_name = db.Column(db.String, nullable=False)
    game_type = db.Column(db.String, nullable=False)
    game_description = db.Column(db.String, nullable=False)

