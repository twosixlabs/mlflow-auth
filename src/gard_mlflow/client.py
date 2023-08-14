import mlflow.server.auth.client
from mlflow.server.auth.entities import User

from .routes import GET_USERS

class AuthClient(mlflow.server.auth.client.AuthServiceClient):

    def list_users(self):
        """
        List all users
        """
        resp = self._request(
            GET_USERS,
            "GET",
        )
        return [User.from_json(u) for u in resp["users"]]
