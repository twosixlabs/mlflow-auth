from flask import Flask
from mlflow.server import app
import mlflow.server.auth

def create_app(app: Flask = app):
    mlflow.server.auth.UNPROTECTED_ROUTES = []
    app = mlflow.server.auth.create_app(app)
    return app
