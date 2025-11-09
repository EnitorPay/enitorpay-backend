from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_session
from app.models.payroll import PayRun, PayRunStatus
from app.schemas.payroll import PayrollCreate, PayrollRead
from typing import List

router = APIRouter(prefix="/api/v1/payroll", tags=["Payroll"])

# ✅ GET all pay runs
@router.get("/", response_model=List[PayrollRead])
def list_payruns(session: Session = Depends(get_session)):
    payruns = session.query(PayRun).all()
    return payruns


# ✅ POST a new pay run
@router.post("/", response_model=PayrollRead)
def create_payrun(data: PayrollCreate, session: Session = Depends(get_session)):
    new_payrun = PayRun(
        company_id=data.company_id,
        period_start=data.period_start,
        period_end=data.period_end,
        check_date=data.check_date,
        status=data.status or PayRunStatus.DRAFT
    )
    session.add(new_payrun)
    session.commit()
    session.refresh(new_payrun)
    return new_payrun
