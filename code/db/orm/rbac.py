from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Rbac(Base):
    __tablename__ = "rbac"

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    role_name: Mapped[str] = mapped_column(String(100), nullable=False)
    role_description: Mapped[str | None] = mapped_column(String(255), nullable=True)
    permission_name: Mapped[str] = mapped_column(String(150), nullable=False)
    permission_description: Mapped[str | None] = mapped_column(String(255), nullable=True)

    __mapper_args__ = {
        "primary_key": [user_id, role_name, permission_name],
    }
