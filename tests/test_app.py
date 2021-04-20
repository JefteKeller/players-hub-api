from flask import Flask


def test_app(sample_app):
    assert isinstance(sample_app, Flask)
