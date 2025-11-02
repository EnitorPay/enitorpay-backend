from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_session
from app.models.payroll import PayRun
from app.models.company import Company
from app.models.employee import Employee
from uuid import UUID
from datetime import date

router = APIRouter(prefix="/api/v1/payroll", tags=["Payroll"])

# ✅ List all pay runs
@router.get("/")
def list_payruns(db: Session = Depends(get_session)):
    runs = db.query(PayRun).all()
    return [
        {
            "id": run.id,
            "company_id": run.company_id,
            "period_start": run.period_start,
            "period_end": run.period_end,
            "check_date": run.check_date,
            "status": run.status,
        }
        for run in runs
    ]


# ✅ Get a single pay run
@router.get("/{payrun_id}")
def get_payrun(payrun_id: UUID, db: Session = Depends(get_session)):
    run = db.query(PayRun).filter(PayRun.id == payrun_id).first()
    if not run:
        raise HTTPException(status_code=404, detail="Pay run not found")
    return {
        "id": run.id,
        "company_id": run.company_id,
        "period_start": run.period_start,
        "period_end": run.period_end,
        "check_date": run.check_date,
        "status": run.status,
    }


# ✅ Create a new pay run
@router.post("/")
def create_payrun(company_id: UUID, period_start: str, period_end: str, check_date: str, db: Session = Depends(get_session)):
    company = db.query(Company).filter(Company.id == company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    new_run = PayRun(
        company_id=company_id,
        period_start=period_start,
        period_end=period_end,
        check_date=check_date,
        status="DRAFT",
    )
    db.add(new_run)
    db.commit()
    db.refresh(new_run)
    return {"message": "Pay run created successfully", "payrun_id": new_run.id}
