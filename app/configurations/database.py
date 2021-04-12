from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from app.models.user_model import UserModel
    from app.models.team_user_model import TeamUserModel
    from app.models.team_model import TeamModel
    from app.models.game_model import GameModel
    from app.models.location_model import LocationModel
    from app.models.match_model import MatchModel