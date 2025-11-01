from __future__ import annotations
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Enum, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID
from .base import Base, TimestampMixin, uuid_pk
import enum

class PayRunStatus(str, enum.Enum):
    DRAFT = "DRAFT"
    CALCULATED = "CALCULATED"
    APPROVED = "APPROVED"
    FINALIZED = "FINALIZED"
    VOIDED = "VOIDED"

class PayRun(Base, TimestampMixin):
    __tablename__ = "pay_run"
    id = uuid_pk()
    company_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    period_start: Mapped[str] = mapped_column(String(10), nullable=False)  # yyyy-mm-dd
    period_end: Mapped[str] = mapped_column(String(10), nullable=False)
    check_date: Mapped[str] = mapped_column(String(10), nullable=False)
    status: Mapped[PayRunStatus] = mapped_column(Enum(PayRunStatus), default=PayRunStatus.DRAFT)
    notes: Mapped[str | None] = mapped_column(Text)

class PayRunEarning(Base, TimestampMixin):
    __tablename__ = "pay_run_earning"
    id = uuid_pk()
    pay_run_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    employee_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    earning_type_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    hours: Mapped[float | None] = mapped_column(Numeric(7,3))
    units: Mapped[float | None] = mapped_column(Numeric(7,3))
    rate: Mapped[float | None] = mapped_column(Numeric(12,4))
    amount: Mapped[float] = mapped_column(Numeric(12,2), nullable=False)

class PayRunTax(Base, TimestampMixin):
    __tablename__ = "pay_run_tax"
    id = uuid_pk()
    pay_run_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    employee_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    tax_code: Mapped[str] = mapped_column(String(30), nullable=False)  # e.g., FIT, FICA_SS_EE
    taxable_wages: Mapped[float] = mapped_column(Numeric(12,2), nullable=False)
    amount: Mapped[float] = mapped_column(Numeric(12,2), nullable=False)
    employer_amount: Mapped[float | None] = mapped_column(Numeric(12,2))

class PayCheckStatus(str, enum.Enum):
    PENDING_PRINT = "PENDING_PRINT"
    PRINTED = "PRINTED"
    VOIDED = "VOIDED"

class PayCheck(Base, TimestampMixin):
    __tablename__ = "pay_check"
    id = uuid_pk()
    pay_run_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    employee_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), nullable=False)

    check_number: Mapped[str | None] = mapped_column(String(40))
    gross_pay: Mapped[float] = mapped_column(Numeric(12,2), nullable=False)
    taxes_total: Mapped[float] = mapped_column(Numeric(12,2), nullable=False)
    deductions_total: Mapped[float] = mapped_column(Numeric(12,2), nullable=False)
    net_pay: Mapped[float] = mapped_column(Numeric(12,2), nullable=False)

    status: Mapped[PayCheckStatus] = mapped_column(Enum(PayCheckStatus), default=PayCheckStatus.PENDING_PRINT)
    printed_at: Mapped[str | None] = mapped_column(String(32))
    stub_pdf_s3_key: Mapped[str | None] = mapped_column(String(300))
