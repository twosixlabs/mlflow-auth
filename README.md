# MLFlow auth extensions

Auth extensions to MLFlow's built-in authentication mechanism to provide better
security and user management.

## Server

MLFlow's built-in authentication allows public signup. While this still helps to
prevent a user from modifying or deleting data belonging to another user, it
doesn't provide any protection against malicious users creating accounts and
uploading massive amounts of data.

The server extension requires admin user access to create users.

MLFlow provides REST APIs for user management, but does not offer any endpoint
to obtain a list of existing users.

The server extension adds the following endpoint to allow for fetching all
users.

| Path | Method |
|------|--------|
| `/api/2.0/mlflow/users` | `GET` |

### Usage

Use `mlflow-auth` as the app name when starting the MLFlow server.

```sh
mlflow server --app-name mlflow-auth
```

## Client

MLFlow's built-in auth service client does not provide any method for obtaining
the list of existing users.

### Usage

```python
import mlflow.server

auth_client = mlflow.server.get_app_client(
    "mlflow-auth", tracking_uri="https://<mlflow_tracking_uri>/"
)
users = auth_client.list_users()
```

## CLI Clients

This package provides a command-line wrapper around the auth client, powered by
[Python Fire](https://github.com/google/python-fire).

Due to the behavior of Python Fire, some commands (those that return an object)
accept a trailing `to-json` to avoid a usage message.

### Usage

All commands require the following environment variables to be set.

```sh
export MLFLOW_TRACKING_USERNAME=admin
export MLFLOW_TRACKING_PASSWORD=password
export MLFLOW_TRACKING_URI=https://<mlflow_tracking_uri>/
```

#### List Users

```sh
mlflow-auth-client list-users --to-json
```

This command requires `--to-json` option to produce meaningful results.

#### Create User

```sh
mlflow-auth-client create-user <username> <password>
# or
mlflow-auth-client create-user <username> <password> to-json
```

The trailing `to-json` is optional, but necessary to avoid getting a usage
message.

#### Fetch User Details

```sh
mlflow-auth-client get-user <username>
# or
mlflow-auth-client get-user <username> to-json
```

The trailing `to-json` is optional, but necessary to avoid getting a usage
message.

#### Promote (or Demote) User to Admin

```sh
# Promotion
mlflow-auth-client update-user-admin <username> True
# Demotion
mlflow-auth-client update-user-admin <username> False
```

#### Change Password

```sh
mlflow-auth-client update-user-password <username> <password>
```

#### Delete User

```sh
mlflow-auth-client delete-user <username>
```

**Note:** If the user has any experiment permissions, those will need to be
revoked before the user can be deleted.

#### Grant Write Permissions To An Experiment

```sh
mlflow-auth-client create-experiment-permission <experiment-id> <username> EDIT
# or
mlflow-auth-client create-experiment-permission <experiment-id> <username> EDIT to-json
```

The trailing `to-json` is optional, but necessary to avoid getting a usage
message.

Use `MANAGE` in place of `EDIT` to provide managing permissions instead of just
write permissions.

Use `update-experiment-permission` in place of `create-experiment-permission` to
change the permission after it has already been created.

#### Remove Permissions To An Experiment

```sh
mlflow-auth-client delete-experiment-permission <experiement-id> <username>
```

