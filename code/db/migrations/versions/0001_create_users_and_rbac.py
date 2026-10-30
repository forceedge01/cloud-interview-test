"""create users and rbac tables

Revision ID: 0001_create_users_and_rbac
Revises:
Create Date: 2026-10-15 00:00:00

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0001_create_users_and_rbac"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("username", sa.String(length=255), nullable=False, unique=True),
        sa.Column("email", sa.String(length=320), nullable=False, unique=True),
        sa.Column("password", sa.String(length=320), nullable=False, unique=True),
    )

    op.create_table(
        "rbac",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("role_name", sa.String(length=100), nullable=False),
        sa.Column("role_description", sa.String(length=255), nullable=True),
        sa.Column("permission_name", sa.String(length=150), nullable=False),
        sa.Column("permission_description", sa.String(length=255), nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("user_id", "role_name", "permission_name"),
    )


def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS rbac")
    op.execute("DROP TABLE IF EXISTS users")
