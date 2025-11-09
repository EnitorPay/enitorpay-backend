from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_session
from app.models import Company
from pydantic import BaseModel
from typing import List
import uuid

router = APIRouter(prefix="/api/v1/companies", tags=["companies"])

class CompanyCreate(BaseModel):
    legal_name: str
    dba_name: str | None = None
    ein: str | None = None
    address_street: str | None = None
    address_city: str | None = None
    address_state: str | None = None
    address_postal: str | None = None

class CompanyRead(CompanyCreate):
    id: uuid.UUID

@router.get("/", response_model=List[CompanyRead])
def list_companies(session: Session = Depends(get_session)):
    companies = session.query(Company).order_by(Company.legal_name).all()
    return companies

@router.post("/", response_model=CompanyRead)
def create_company(data: CompanyCreate, session: Session = Depends(get_session)):
    new_company = Company(**data.model_dump())
    session.add(new_company)
    session.commit()
    session.refresh(new_company)
    return new_company
