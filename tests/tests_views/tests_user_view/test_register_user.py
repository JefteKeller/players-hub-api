from flask.testing import FlaskClient


def test_register_user(app_client: FlaskClient):
    response = app_client.post(
        "/register/",
        json={
            "nickname": "test",
            "first_name": "jj",
            "last_name": "tt",
            "email": "jj@test.com",
            "password": "1234",
            "biography": "Python is KING",
        },
    )
    assert response.status_code == 409
