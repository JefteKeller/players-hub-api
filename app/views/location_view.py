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
        "Location": {
            "location_name": new_location.location_name,
            "location_phone": new_location.location_phone,
        }
    }, HTTPStatus.CREATED


@bp_location.route("/", methods=["GET"], strict_slashes=False)
@jwt_required()
def list_locations():
    locations_query = LocationModel.query.all()

    return {
        "Locations": [
            {
                "id": location.id,
                "location_name": location.location_name,
                "location_phone": location.location_phone,
            }
            for location in locations_query
        ]
    }, HTTPStatus.OK


@bp_location.route("/<int:location_id>", methods=["GET"], strict_slashes=False)
@jwt_required()
def get_location(location_id):

    search_location = LocationModel.query.filter_by(id=location_id).first()

    return {
        "location": {
            "location_name": search_location.location_name,
            "location_phone": search_location.location_phone,
        }
    }, HTTPStatus.OK


@bp_location.route("/<int:location_id>", methods=["PATCH"], strict_slashes=False)
@jwt_required()
def update_location(location_id):
    session = current_app.db.session

    data = request.get_json()

    location_name = data.get("location_name")
    location_phone = data.get("location_phone")

    location_to_update: LocationModel = LocationModel.query.filter_by(
        id=location_id
    ).update(dict(location_name=location_name, location_phone=location_phone))

    if not location_to_update:
        return {"error": "Location not found"}, HTTPStatus.NOT_FOUND

    location_updated = LocationModel(
        location_name=location_name, location_phone=location_phone
    )

    session.commit()

    return {
        "location": {
            "location_name": location_updated.location_name,
            "location_phone": location_updated.location_phone,
        }
    }, HTTPStatus.OK
