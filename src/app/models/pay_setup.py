from __future__ import annotations
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Enum, Numeric
from sqlalchemy.dialects.postgresql import UUID
from .base import Base, TimestampMixin, uuid_pk
import enum

class PayType(str, enum.Enum):
    HOURLY = "HOURLY"
    SALARY = "SALARY"

class EmployeePaySetup(Base, TimestampMixin):
    __tablename__ = "employee_pay_setup"
    id = uuid_pk()
    employee_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), nullable=False)

    pay_type: Mapped[PayType] = mapped_column(Enum(PayType), nullable=False)
    hourly_rate: Mapped[float | None] = mapped_column(Numeric(12,2))
    salary_amount: Mapped[float | None] = mapped_column(Numeric(12,2))
    standard_hours_per_period: Mapped[float | None] = mapped_column(Numeric(7,2))

    # Tax profile (initial pass; we’ll refine per state later)
    filing_status_fed: Mapped[str | None] = mapped_column(String(30))
    dependents_fed: Mapped[int | None]
    additional_withholding_fed: Mapped[float | None] = mapped_column(Numeric(12,2))

    state_primary: Mapped[str | None] = mapped_column(String(2))
    filing_status_state: Mapped[str | None] = mapped_column(String(30))
    dependents_state: Mapped[int | None]
    additional_withholding_state: Mapped[float | None] = mapped_column(Numeric(12,2))

    ca_sdi_exempt: Mapped[bool | None]
