from flask import Flask
from mlflow.server import app
import mlflow.server.auth

def create_app(app: Flask = app):
    # Restrict user creation to admins only
    mlflow.server.auth.UNPROTECTED_ROUTES = []
    mlflow.server.auth.BEFORE_REQUEST_VALIDATORS.update({
        (mlflow.server.auth.SIGNUP, "GET"): mlflow.server.auth.validate_can_update_user_admin,
        (mlflow.server.auth.CREATE_USER, "POST"): mlflow.server.auth.validate_can_update_user_admin,
    })
    app = mlflow.server.auth.create_app(app)
    return app
