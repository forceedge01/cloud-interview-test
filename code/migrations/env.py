from __future__ import annotations

import os
from pathlib import Path
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

from orm.base import Base
from orm.database import database_url
from orm.user import User  # noqa: F401
from orm.rbac import Rbac  # noqa: F401

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)


def _load_dotenv() -> None:
    dotenv_path = Path(__file__).resolve().parent.parent / ".env"
    if not dotenv_path.exists():
        return

    for line in dotenv_path.read_text().splitlines():
        raw = line.strip()
        if not raw or raw.startswith("#") or "=" not in raw:
            continue
        key, value = raw.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


_load_dotenv()
# render_as_string keeps special characters in the password URL-encoded;
# "%" is doubled because alembic config values go through configparser.
config.set_main_option(
    "sqlalchemy.url",
    database_url().render_as_string(hide_password=False).replace("%", "%%"),
)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
