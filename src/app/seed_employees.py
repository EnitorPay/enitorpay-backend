from sqlalchemy.orm import Session
from app.db import get_engine
from app.models.company import Company
from app.models.employee import Employee  # if not found, we’ll adjust import
from sqlalchemy import select

def seed_employees():
    engine = get_engine()
    with Session(engine) as session:
        # Get the Enitor Test Co. company
        company = session.scalar(select(Company).where(Company.legal_name == "Enitor Test Co."))
        if not company:
            print("❌ Company 'Enitor Test Co.' not found.")
            return

        # Add employees if table is empty
        existing = session.execute(select(Employee)).scalars().all()
        if existing:
            print("✅ Employees already exist, skipping seeding.")
            return

        employees = [
            Employee(first_name="Juan", last_name="Martinez", company_id=company.id),
            Employee(first_name="Sara", last_name="Lopez", company_id=company.id),
            Employee(first_name="Tom", last_name="Andrews", company_id=company.id),
        ]

        session.add_all(employees)
        session.commit()
        print("🌱 Seeded employees successfully!")

if __name__ == "__main__":
    seed_employees()
