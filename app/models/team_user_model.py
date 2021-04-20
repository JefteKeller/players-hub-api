# // Disabling errors of ORM type due to how SQLAlchemy works
# type: ignore

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
