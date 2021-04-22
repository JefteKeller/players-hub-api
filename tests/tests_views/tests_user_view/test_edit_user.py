from flask.testing import FlaskClient
from http import HTTPStatus


USERS_ROUTE = "/users"


def test_edit_should_fail_when_email_already_exists(
    sample_app, app_client: FlaskClient, test_token
):
    with sample_app.test_request_context():

        expected_response = {"error": "This email address is already being used"}

        response = app_client.patch(
            USERS_ROUTE,
            json={
                "email": "bebeto@gmail.com",
            },
            headers=test_token,
        )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.get_json() == expected_response


def test_edit_should_fail_when_user_not_exists(
    sample_app, app_client: FlaskClient, test_token_user_not_exists
):
    with sample_app.test_request_context():

        expected_response = {"error": "User not found"}

        response = app_client.patch(
            USERS_ROUTE,
            json={},
            headers=test_token_user_not_exists,
        )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.get_json() == expected_response


def test_edit_should_change_user_info(sample_app, app_client: FlaskClient, test_token):
    with sample_app.test_request_context():

        expected_response = {
            "user": {
                "email": "bebeto@gmail.com",
                "nickname": "LuanGameplays",
                "first_name:": "Ze",
                "last_name": "Neves",
                "biography": "Peace",
            }
        }

        response = app_client.patch(
            USERS_ROUTE,
            json={
                "nickname": "LuanGameplays",
                "first_name": "Ze",
                "biography": "Peace",
            },
            headers=test_token,
        )

    assert response.status_code == HTTPStatus.OK
    assert response.get_json() == expected_response
