from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from enum import Enum


class PayRunStatus(str, Enum):
    DRAFT = "DRAFT"
    CALCULATED = "CALCULATED"
    APPROVED = "APPROVED"
    FINALIZED = "FINALIZED"
    VOIDED = "VOIDED"


class PayrollBase(BaseModel):
    company_id: UUID
    period_start: str
    period_end: str
    check_date: str
    status: Optional[PayRunStatus] = PayRunStatus.DRAFT


class PayrollCreate(PayrollBase):
    pass


class PayrollRead(PayrollBase):
    id: UUID

    class Config:
        from_attributes = True
