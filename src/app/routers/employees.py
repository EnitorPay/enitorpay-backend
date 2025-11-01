from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_session
from app.models.employee import Employee
from app.models.company import Company
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

@router.post("/")
def create_employee(data: dict, session: Session = Depends(get_session)):
    company = session.get(Company, data.get("company_id"))
    if not company:
        raise HTTPException(status_code=400, detail="Invalid company ID")

    new_employee = Employee(
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        company_id=data.get("company_id")
    )
    session.add(new_employee)
    session.commit()
    session.refresh(new_employee)
    return {"id": new_employee.id, "message": "Employee created successfully"}

