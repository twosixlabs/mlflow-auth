import mlflow.server.auth.client
from mlflow.server.auth.entities import User

from .routes import GET_USERS

class AuthClient(mlflow.server.auth.client.AuthServiceClient):

    def list_users(self, to_json = False):
        """
        List all users.

        :param to_json: Return list of users as JSON objects.

        :return: List of :py:class:`mlflow.server.auth.entities.User` objects,
                 or a list of JSON objects if `to_json` is `True`.

        .. code-block:: bash
            :caption: Example

            export MLFLOW_TRACKING_USERNAME=admin
            export MLFLOW_TRACKING_PASSWORD=password

        .. code-block:: python

            from gard_mlflow.client import AuthClient

            client = AuthClient("tracking_uri")
            users = client.list_users()

            for user in users:
                print("----")
                print("user_id: {}".format(user.id))
                print("username: {}".format(user.username))
                print("password_hash: {}".format(user.password_hash))
                print("is_admin: {}".format(user.is_admin))

        .. code-block:: text
            :caption: Output

            ----
            user_id: 1
            username: admin
            password_hash: REDACTED
            is_admin: True
            ----
            user_id: 3
            username: newuser
            password_hash: REDACTED
            is_admin: False
        """
        resp = self._request(
            GET_USERS,
            "GET",
        )
        if to_json:
            return resp["users"]
        return [User.from_json(u) for u in resp["users"]]
