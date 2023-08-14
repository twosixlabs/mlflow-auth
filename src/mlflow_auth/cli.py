import os
import sys

import fire
import mlflow
import mlflow.server


def client():
    """Perform MLFlow client functions"""
    client = mlflow.MlflowClient()
    fire.Fire(client)


def auth_client():
    """Perform MLFlow auth client functions"""
    tracking_uri = os.environ.get("MLFLOW_TRACKING_URI")
    if not tracking_uri:
        print("Must set MLFLOW_TRACKING_URI environment variable")
        sys.exit(-1)
    client = mlflow.server.get_app_client("mlflow-auth", tracking_uri=tracking_uri)
    fire.Fire(client)
