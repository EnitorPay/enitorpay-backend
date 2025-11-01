from __future__ import annotations 
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Enum, ARRAY, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from .base import Base, TimestampMixin, uuid_pk
import enum

class CheckLayout(str, enum.Enum):
    TOP_SINGLE_STUB = "TOP_SINGLE_STUB"
    BOTTOM_SINGLE_STUB = "BOTTOM_SINGLE_STUB"  # default for EnitorPay

class PaySchedule(str, enum.Enum):
    WEEKLY = "WEEKLY"
    BIWEEKLY = "BIWEEKLY"
    SEMI_MONTHLY = "SEMI_MONTHLY"
    MONTHLY = "MONTHLY"

class Company(Base, TimestampMixin):
    __tablename__ = "company"
    id = uuid_pk()
    legal_name: Mapped[str] = mapped_column(String(200), nullable=False)
    dba_name: Mapped[str | None] = mapped_column(String(200))
    ein: Mapped[str | None] = mapped_column(String(15))

    address_street: Mapped[str | None] = mapped_column(String(200))
    address_city: Mapped[str | None] = mapped_column(String(100))
    address_state: Mapped[str | None] = mapped_column(String(2))
    address_postal: Mapped[str | None] = mapped_column(String(15))

    default_check_layout: Mapped[CheckLayout] = mapped_column(
        Enum(CheckLayout), nullable=False, default=CheckLayout.BOTTOM_SINGLE_STUB
    )
    default_pay_schedule: Mapped[PaySchedule | None] = mapped_column(Enum(PaySchedule))

    states_of_operation: Mapped[list[str] | None] = mapped_column(ARRAY(String), nullable=True)

    # Relationship to employees (requires FK on employee.company_id)
    employees: Mapped[list["Employee"]] = relationship(
        back_populates="company",
        cascade="all, delete-orphan"
    )
