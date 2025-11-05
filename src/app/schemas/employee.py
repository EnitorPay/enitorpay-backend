from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    company_id: UUID

class EmployeeCreate(EmployeeBase):
    middle_name: Optional[str] = None
    ssn_encrypted: Optional[str] = None
    dob: Optional[str] = None
    hire_date: Optional[str] = None
    term_date: Optional[str] = None
    address_street: Optional[str] = None
    address_city: Optional[str] = None
    address_state: Optional[str] = None
    address_postal: Optional[str] = None

class EmployeeRead(EmployeeBase):
    id: UUID

    class Config:
        orm_mode = True
