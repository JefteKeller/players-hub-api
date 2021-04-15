from flask import Flask
from pytest import fixture

from app import create_app


@fixture
def sample_app():
    yield create_app()


@fixture
def app_client(sample_app: Flask):
    yield sample_app.test_client()
