from sqlalchemy.orm import Session
from app.db import get_engine
from app.models import (
    Company, Employee, EmployeeStatus,
    EmployeePaySetup, PayType,
    PayRun, PayRunEarning, PayRunTax, PayCheck
)
from sqlalchemy import select
from datetime import date
import uuid

def seed_demo_data():
    engine = get_engine()
    with Session(engine) as session:
        # 1️⃣ Company
        company = Company(
            legal_name="Enitor Test Co.",
            dba_name="Enitor Payroll Demo",
            ein="12-3456789",
            address_street="123 Sunrise Ave",
            address_city="Portland",
            address_state="OR",
            address_postal="97201"
        )
        session.add(company)
        session.flush()  # assign ID

        # 2️⃣ Employees
        emp_hourly = Employee(
            company_id=company.id,
            status=EmployeeStatus.ACTIVE,
            first_name="Maria",
            last_name="Lopez",
            ssn_encrypted="XXX-XX-1234",
            hire_date=str(date(2024, 6, 1))
        )

        emp_salary = Employee(
            company_id=company.id,
            status=EmployeeStatus.ACTIVE,
            first_name="David",
            last_name="Nguyen",
            ssn_encrypted="XXX-XX-5678",
            hire_date=str(date(2023, 11, 10))
        )

        session.add_all([emp_hourly, emp_salary])
        session.flush()

        # 3️⃣ Pay setups
        pay_hourly = EmployeePaySetup(
            employee_id=emp_hourly.id,
            pay_type=PayType.HOURLY,
            hourly_rate=25.00,
            standard_hours_per_period=80
        )
        pay_salary = EmployeePaySetup(
            employee_id=emp_salary.id,
            pay_type=PayType.SALARY,
            salary_amount=4000.00
        )
        session.add_all([pay_hourly, pay_salary])
        session.flush()

        # 4️⃣ Pay run
        payrun = PayRun(
            company_id=company.id,
            period_start="2024-10-01",
            period_end="2024-10-15",
            check_date="2024-10-18",
        )
        session.add(payrun)
        session.flush()

        # 5️⃣ Earnings
        earn1 = PayRunEarning(
            pay_run_id=payrun.id,
            employee_id=emp_hourly.id,
            earning_type_id=uuid.uuid4(),
            hours=80, rate=25, amount=2000.00
        )
        earn2 = PayRunEarning(
            pay_run_id=payrun.id,
            employee_id=emp_salary.id,
            earning_type_id=uuid.uuid4(),
            amount=2000.00
        )
        session.add_all([earn1, earn2])
        session.flush()

        # 6️⃣ Taxes (simplified)
        tax1 = PayRunTax(
            pay_run_id=payrun.id,
            employee_id=emp_hourly.id,
            tax_code="FIT",
            taxable_wages=2000.00,
            amount=150.00
        )
        tax2 = PayRunTax(
            pay_run_id=payrun.id,
            employee_id=emp_salary.id,
            tax_code="FIT",
            taxable_wages=2000.00,
            amount=200.00
        )
        session.add_all([tax1, tax2])
        session.flush()

        # 7️⃣ Checks
        check1 = PayCheck(
            pay_run_id=payrun.id,
            employee_id=emp_hourly.id,
            check_number="1001",
            gross_pay=2000.00,
            taxes_total=150.00,
            deductions_total=0.00,
            net_pay=1850.00
        )
        check2 = PayCheck(
            pay_run_id=payrun.id,
            employee_id=emp_salary.id,
            check_number="1002",
            gross_pay=2000.00,
            taxes_total=200.00,
            deductions_total=0.00,
            net_pay=1800.00
        )
        session.add_all([check1, check2])
        session.commit()

        print("✅ Demo data inserted successfully!")

if __name__ == "__main__":
    seed_demo_data()
