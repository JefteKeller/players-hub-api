from flask import Flask
from flask.testing import FlaskClient


def test_app(sample_app):
    assert isinstance(sample_app, Flask)
