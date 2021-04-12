from sqlalchemy.orm import backref

from . import db


class TeamModel(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String, nullable=False)
    team_description = db.Column(db.String, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship(
        "UserModel",
        uselist=False,
        lazy="joined",
        backref=db.backref(
            "team",
            lazy="joined",
        ),
    )