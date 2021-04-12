from sqlalchemy.orm import backref
from werkzeug.security import generate_password_hash, check_password_hash

from . import db


class LocationModel(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String, nullable=False)
    location_phone = db.Column(db.String, nullable=False)

    match_id = db.Column(db.Integer, db.ForeignKey("matches.id"))
    match = db.relationship(
        "MatchModel",
        uselist=False,
        lazy="joined",
        backref=db.backref(
            "location",
            lazy="joined",
        ),
    )
