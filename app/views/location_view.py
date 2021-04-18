from flask import Blueprint, request, current_app
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
)
from http import HTTPStatus
from datetime import timedelta

from app.models.location_model import LocationModel


bp_location = Blueprint("location_view", __name__, url_prefix="/locations")


@bp_location.route("/", methods=["POST"], strict_slashes=False)
@jwt_required()
def register_location():
    session = current_app.db.session

    res = request.get_json()
    location_name = res.get("location_name")
    location_phone = res.get("location_phone")

    new_location = LocationModel(
        location_name=location_name, location_phone=location_phone
    )

    session.add(new_location)

    session.commit()

    return {
        "location": {
            "location_name": new_location.location_name,
            "location_phone": new_location.location_phone,
        }
    }, HTTPStatus.CREATED


@bp_location.route("/", methods=["GET"], strict_slashes=False)
@jwt_required()
def list_locations():
    return {"msg": "Teste list locations"}, HTTPStatus.OK


@bp_location.route("/get/", methods=["GET"], strict_slashes=False)
@jwt_required()
def get_location():
    return {"msg": "Teste get location"}, HTTPStatus.OK


@bp_location.route("/", methods=["PATCH", "PUT"], strict_slashes=False)
@jwt_required()
def update_location():
    return {"msg": "Teste update location"}, HTTPStatus.OK
