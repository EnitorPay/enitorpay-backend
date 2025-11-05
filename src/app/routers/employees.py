from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_session
from app.models.employee import Employee
from app.models.company import Company
from app.schemas.employee import EmployeeCreate, EmployeeRead
from typing import List

router = APIRouter(prefix="/api/v1/employees", tags=["Employees"])


@router.get("/", response_model=List[EmployeeRead])
def list_employees(session: Session = Depends(get_session)):
    employees = session.query(Employee).all()
    return employees


@router.get("/{employee_id}", response_model=EmployeeRead)
def get_employee(employee_id: str, session: Session = Depends(get_session)):
    employee = session.get(Employee, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@router.post("/", response_model=EmployeeRead)
def create_employee(data: EmployeeCreate, session: Session = Depends(get_session)):
    company = session.get(Company, data.company_id)
    if not company:
        raise HTTPException(status_code=400, detail="Invalid company ID")

    new_employee = Employee(**data.dict())
    session.add(new_employee)
    session.commit()
    session.refresh(new_employee)
    return new_employee
