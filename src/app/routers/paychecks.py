from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_session
from app.models.payroll import PayCheck
from app.schemas.paycheck import PayCheckCreate, PayCheckRead

router = APIRouter(prefix="/api/v1/paychecks", tags=["Paychecks"])


# ✅ GET — list all paychecks
@router.get("/", response_model=List[PayCheckRead])
def list_paychecks(session: Session = Depends(get_session)):
    paychecks = session.query(PayCheck).all()
    return paychecks


# ✅ POST — create a new paycheck
@router.post("/", response_model=PayCheckRead)
def create_paycheck(data: PayCheckCreate, session: Session = Depends(get_session)):
    new_check = PayCheck(
        employee_id=data.employee_id,
        pay_run_id=data.pay_run_id,
        gross_pay=data.gross_pay,
        net_pay=data.net_pay,
        status=data.status or "PENDING"
    )
    session.add(new_check)
    session.commit()
    session.refresh(new_check)
    return new_check
