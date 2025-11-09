from pydantic import BaseModel
from uuid import UUID
from datetime import date
from typing import Optional


class PayCheckBase(BaseModel):
    employee_id: UUID
    pay_run_id: UUID
    gross_pay: float
    net_pay: float
    pay_date: date
    status: Optional[str] = "DRAFT"


class PayCheckCreate(PayCheckBase):
    pass


class PayCheckRead(PayCheckBase):
    id: UUID

    class Config:
        from_attributes = True
