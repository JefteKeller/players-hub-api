# // Disabling errors of ORM type due to how SQLAlchemy works
# type: ignore
from datetime import datetime

from . import db


class CommentModel(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(140), nullable=False)
    author = db.Column(db.String(32), nullable=False)
    timestamp = db.Column(db.DateTime(), default=datetime.utcnow, index=True)

    match_id = db.Column(db.Integer, db.ForeignKey("matches.id"))

    match = db.relationship(
        "MatchModel",
        uselist=False,
        lazy="select",
        backref=db.backref("comments", lazy="select"),
    )
