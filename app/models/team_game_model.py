# // Disabling errors of ORM type due to how SQLAlchemy works
# type: ignore

from . import db


class TeamGameModel(db.Model):
    __tablename__ = "team_games"

    id = db.Column(db.Integer, primary_key=True)

    game_id = db.Column(db.Integer, db.ForeignKey("games.id"))
    game = db.relationship(
        "GameModel",
        uselist=False,
        lazy="joined",
        backref=db.backref(
            "team_game",
            lazy="joined",
        ),
    )

    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))
    team = db.relationship(
        "TeamModel",
        uselist=False,
        lazy="joined",
        backref=db.backref(
            "team_game",
            lazy="joined",
        ),
    )
