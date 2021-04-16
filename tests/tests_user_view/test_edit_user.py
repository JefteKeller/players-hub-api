from flask.testing import FlaskClient

from pytest import fixture
from http import HTTPStatus


@fixture(scope="module")
def header_with_jwt_auth_token():
    yield "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxODU0NTU5OSwianRpIjoiZWExODM1MDUtNGNlMy00MjEwLTlhMjgtZDkzMjM2ZTJkNjY2IiwibmJmIjoxNjE4NTQ1NTk5LCJ0eXBlIjoiYWNjZXNzIiwic3ViIjo1LCJleHAiOjE2MTkxNTAzOTl9.mF8pVBIUAojdngPCOZc4ddOiCcIs97nk2bQ_FtYGpMs"


def test_edit_should_fail_when_email_already_exists(
    app_client: FlaskClient, header_with_jwt_auth_token
):
    response = app_client.patch(
        "/users",
        json={
            "first_name": "bebeto222@gmail.com",
        },
        headers={"Authorization": f"Bearer {header_with_jwt_auth_token}"},
    )
    assert response.status_code == HTTPStatus.CONFLICT


# "nickname": "test",
#             "first_name": "jj",
#             "last_name": "tt",
#   "password": "1234",
