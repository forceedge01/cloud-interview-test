import json
import os
import time

from sqlalchemy import create_engine, event
from sqlalchemy.engine import URL, Engine

# RDS-managed secrets rotate, so re-read the secret periodically rather than
# caching the password for the lifetime of the process.
SECRET_TTL_SECONDS = 300

_secret_cache: dict = {"credentials": None, "expires_at": 0.0}


def _secret_credentials(secret_id: str) -> tuple[str, str]:
    now = time.monotonic()
    if _secret_cache["credentials"] is None or now >= _secret_cache["expires_at"]:
        import boto3

        response = boto3.client("secretsmanager").get_secret_value(SecretId=secret_id)
        secret = json.loads(response["SecretString"])
        _secret_cache["credentials"] = (secret["username"], secret["password"])
        _secret_cache["expires_at"] = now + SECRET_TTL_SECONDS
    return _secret_cache["credentials"]


def db_credentials() -> tuple[str | None, str | None]:
    """Username and password from Secrets Manager when DB_SECRET_ID is set,
    otherwise from the DB_USER / DB_PASSWORD environment variables."""
    secret_id = os.getenv("DB_SECRET_ID")
    if secret_id:
        return _secret_credentials(secret_id)
    return os.getenv("DB_USER"), os.getenv("DB_PASSWORD")


def database_url() -> URL:
    username, password = db_credentials()
    return URL.create(
        "mysql+pymysql",
        username=username,
        password=password,
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=int(os.getenv("DB_PORT", "3306")),
        database=os.getenv("DB_NAME", "interview_db"),
    )


def create_db_engine() -> Engine:
    engine = create_engine(database_url(), pool_pre_ping=True)

    @event.listens_for(engine, "do_connect")
    def _use_current_credentials(dialect, conn_rec, cargs, cparams):
        # Every new pooled connection picks up the latest (possibly rotated) password.
        cparams["user"], cparams["password"] = db_credentials()

    return engine
