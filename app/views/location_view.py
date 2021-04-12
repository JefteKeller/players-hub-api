from flask import Blueprint, request, current_app
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)
from http import HTTPStatus
from datetime import timedelta

from app.models.location_model import LocationModel


bp_location = Blueprint("location_view", __name__, url_prefix="/locations")

@bp_location.route("/", methods=["POST"])
@jwt_required()
def register_location():
    return {"msg": "Teste register location"}, HTTPStatus.OK

@bp_location.route("/", methods=["GET"])
@jwt_required()
def list_locations():
    return {"msg": "Teste list locations"}, HTTPStatus.OK

@bp_location.route("/get/", methods=["GET"])
@jwt_required()
def get_location():
    return {"msg": "Teste get location"}, HTTPStatus.OK


@bp_location.route("/", methods=["PATCH", "PUT"])
@jwt_required()
def update_location():
    return {"msg": "Teste update location"}, HTTPStatus.OK