from __future__ import annotations
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from .base import Base, TimestampMixin, uuid_pk
import enum


class EmployeeStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    TERMINATED = "TERMINATED"


class Employee(Base, TimestampMixin):
    __tablename__ = "employee"

    id = uuid_pk()
    company_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("company.id", ondelete="CASCADE"),
        nullable=False
    )

    status: Mapped[EmployeeStatus] = mapped_column(
        Enum(EmployeeStatus),
        default=EmployeeStatus.ACTIVE
    )

    first_name: Mapped[str] = mapped_column(String(80), nullable=False)
    last_name: Mapped[str] = mapped_column(String(80), nullable=False)
    middle_name: Mapped[str | None] = mapped_column(String(80))

    ssn_encrypted: Mapped[str | None] = mapped_column(String(200))
    dob: Mapped[str | None] = mapped_column(String(10))   # yyyy-mm-dd
    hire_date: Mapped[str | None] = mapped_column(String(10))
    term_date: Mapped[str | None] = mapped_column(String(10))

    address_street: Mapped[str | None] = mapped_column(String(200))
    address_city: Mapped[str | None] = mapped_column(String(100))
    address_state: Mapped[str | None] = mapped_column(String(2))
    address_postal: Mapped[str | None] = mapped_column(String(15))

    company: Mapped["Company"] = relationship(back_populates="employees")
