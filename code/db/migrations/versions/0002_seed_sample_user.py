"""seed sample user and permissions

Revision ID: 0002_seed_sample_user
Revises: 0001_create_users_and_rbac
Create Date: 2026-10-15 00:01:00

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0002_seed_sample_user"
down_revision = "0001_create_users_and_rbac"
branch_labels = None
depends_on = None


def upgrade() -> None:
    users = sa.table(
        "users",
        sa.column("id", sa.Integer),
        sa.column("username", sa.String),
        sa.column("email", sa.String),
    )

    rbac = sa.table(
        "rbac",
        sa.column("user_id", sa.Integer),
        sa.column("role_name", sa.String),
        sa.column("role_description", sa.String),
        sa.column("permission_name", sa.String),
        sa.column("permission_description", sa.String),
    )

    op.bulk_insert(
        users,
        [
            {
                "id": 1,
                "username": "alice",
                "email": "alice@example.com",
            }
        ],
    )

    op.bulk_insert(
        rbac,
        [
            {
                "user_id": 1,
                "role_name": "admin",
                "role_description": "Administrator role",
                "permission_name": "users:read",
                "permission_description": "Read users",
            },
            {
                "user_id": 1,
                "role_name": "admin",
                "role_description": "Administrator role",
                "permission_name": "users:write",
                "permission_description": "Write users",
            },
            {
                "user_id": 1,
                "role_name": "admin",
                "role_description": "Administrator role",
                "permission_name": "reports:read",
                "permission_description": "Read reports",
            },
        ],
    )


def downgrade() -> None:
    op.execute("DELETE FROM rbac WHERE user_id = 1")
    op.execute("DELETE FROM users WHERE id = 1")
