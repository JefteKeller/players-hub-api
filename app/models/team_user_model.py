from sqlalchemy.orm import backref
from werkzeug.security import generate_password_hash, check_password_hash

from . import db


class TeamUserModel(db.Model):
    __tablename__ = "team_users"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship(
        "UserModel",
        uselist=False,
        lazy="joined",
        backref=db.backref(
            "team_user",
            lazy="joined",
        ),
    )

    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))
    team = db.relationship(
        "TeamModel",
        uselist=False,
        lazy="joined",
        backref=db.backref(
            "team_user",
            lazy="joined",
        ),
    )