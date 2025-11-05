from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_session
from app.models.employee import Employee
from app.models.company import Company
from app.schemas.employee import EmployeeCreate, EmployeeRead
from typing import List

router = APIRouter(prefix="/api/v1/employees", tags=["Employees"])


@router.get("/", response_model=List[dict])
def list_employees(session: Session = Depends(get_session)):
    employees = session.query(Employee).all()
    return [
        {
            "id": e.id,
            "first_name": e.first_name,
            "last_name": e.last_name,
            "company_id": e.company_id
        }
        for e in employees
    ]


@router.get("/{employee_id}")
def get_employee(employee_id: str, session: Session = Depends(get_session)):
    employee = session.get(Employee, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {
        "id": employee.id,
        "first_name": employee.first_name,
        "last_name": employee.last_name,
        "company_id": employee.company_id
    }


@router.post("/", response_model=EmployeeRead)
def create_employee(employee: EmployeeCreate, session: Session = Depends(get_session)):
    # ✅ Validate the company exists
    company = session.get(Company, employee.company_id)
    if not company:
        raise HTTPException(status_code=400, detail="Invalid company ID")

    db_employee = Employee(**employee.dict())
    session.add(db_employee)
    session.commit()
    session.refresh(db_employee)
    return db_employee
