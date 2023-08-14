from flask import Flask, make_response
from mlflow.server import app
import mlflow.server.auth
from mlflow.server.handlers import _get_rest_path, catch_mlflow_exception


GET_USERS = _get_rest_path("/mlflow/users")


def create_app(app: Flask = app):
    # Restrict user creation to admins only
    mlflow.server.auth.UNPROTECTED_ROUTES = []
    mlflow.server.auth.BEFORE_REQUEST_VALIDATORS.update({
        (mlflow.server.auth.SIGNUP, "GET"): mlflow.server.auth.validate_can_update_user_admin,
        (mlflow.server.auth.CREATE_USER, "POST"): mlflow.server.auth.validate_can_update_user_admin,
        (GET_USERS, "GET"): mlflow.server.auth.validate_can_update_user_admin,
    })
    app = mlflow.server.auth.create_app(app)
    app.add_url_rule(
        rule=GET_USERS,
        view_func=get_users,
        methods=["GET"],
    )
    return app


@catch_mlflow_exception
def get_users():
    users = mlflow.server.auth.store.list_users()
    return make_response({"users": [u.to_json() for u in users]})
