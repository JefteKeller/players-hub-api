# // Disabling errors of ORM type due to how SQLAlchemy works
# type: ignore

from . import db
from datetime import datetime


class MatchModel(db.Model):
    __tablename__ = "matches"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    match_register_date = db.Column(db.DateTime(), default=datetime.utcnow, index=True)

    match_winner_id = db.Column(db.Integer, db.ForeignKey("teams.id"))
    team_id_1 = db.Column(db.Integer, db.ForeignKey("teams.id"))
    team_id_2 = db.Column(db.Integer, db.ForeignKey("teams.id"))

    game_id = db.Column(db.Integer, db.ForeignKey("games.id"))
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"))

    match_winner = db.relationship(
        "TeamModel",
        uselist=False,
        lazy="select",
        backref=db.backref(
            "match_winner",
            lazy="select",
        ),
        foreign_keys=[match_winner_id],
    )

    team_1 = db.relationship(
        "TeamModel",
        uselist=False,
        lazy="select",
        backref=db.backref(
            "match_team_1",
            lazy="select",
        ),
        foreign_keys=[team_id_1],
    )

    team_2 = db.relationship(
        "TeamModel",
        uselist=False,
        lazy="select",
        backref=db.backref(
            "match_team_2",
            lazy="select",
        ),
        foreign_keys=[team_id_2],
    )

    game = db.relationship(
        "GameModel",
        uselist=False,
        lazy="select",
        backref=db.backref(
            "match",
            lazy="select",
        ),
    )

    location = db.relationship(
        "LocationModel",
        uselist=False,
        lazy="select",
        backref=db.backref(
            "match",
            lazy="select",
        ),
    )
