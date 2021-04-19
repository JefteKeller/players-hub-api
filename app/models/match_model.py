# // Disabling errors of ORM type due to how SQLAlchemy works
# type: ignore

from . import db


class MatchModel(db.Model):
    __tablename__ = "matches"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)

    match_winner_id = db.Column(db.Integer, db.ForeignKey("teams.id"))
    team_id_1 = db.Column(db.Integer, db.ForeignKey("teams.id"))
    team_id_2 = db.Column(db.Integer, db.ForeignKey("teams.id"))

    match_winner = db.relationship(
        "TeamModel",
        uselist=False,
        lazy="joined",
        backref=db.backref(
            "match_winner",
            lazy="joined",
        ),
        foreign_keys=[match_winner_id],
    )

    team_1 = db.relationship(
        "TeamModel",
        uselist=False,
        lazy="joined",
        backref=db.backref(
            "match_team_1",
            lazy="joined",
        ),
        foreign_keys=[team_id_1],
    )

    team_2 = db.relationship(
        "TeamModel",
        uselist=False,
        lazy="joined",
        backref=db.backref(
            "match_team_2",
            lazy="joined",
        ),
        foreign_keys=[team_id_2],
    )

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

    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"))
    location = db.relationship(
        "LocationModel",
        uselist=False,
        lazy="joined",
        backref=db.backref(
            "match",
            lazy="joined",
        ),
    )
