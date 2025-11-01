from __future__ import annotations
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean, Numeric
from .base import Base, TimestampMixin, uuid_pk

class EarningType(Base, TimestampMixin):
    __tablename__ = "earning_type"
    id = uuid_pk()
    company_id: Mapped[str] = mapped_column(String(36), nullable=False)
    code: Mapped[str] = mapped_column(String(20), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str | None] = mapped_column(String(200))

    subject_fit: Mapped[bool] = mapped_column(Boolean, default=True)
    subject_ss: Mapped[bool] = mapped_column(Boolean, default=True)
    subject_medicare: Mapped[bool] = mapped_column(Boolean, default=True)
    subject_futa: Mapped[bool] = mapped_column(Boolean, default=True)
    subject_state: Mapped[bool] = mapped_column(Boolean, default=True)

class DeductionType(Base, TimestampMixin):
    __tablename__ = "deduction_type"
    id = uuid_pk()
    company_id: Mapped[str] = mapped_column(String(36), nullable=False)
    code: Mapped[str] = mapped_column(String(20), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str | None] = mapped_column(String(200))

    pre_tax_fit: Mapped[bool] = mapped_column(Boolean, default=False)
    pre_tax_fica: Mapped[bool] = mapped_column(Boolean, default=False)
    pre_tax_state: Mapped[bool] = mapped_column(Boolean, default=False)
    annual_limit: Mapped[float | None] = mapped_column(Numeric(12,2))
