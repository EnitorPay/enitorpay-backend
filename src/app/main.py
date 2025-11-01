from fastapi import FastAPI
from app.routers import health, companies, employees

app = FastAPI(title="EnitorPay API", version="0.1.0")

# Routers
app.include_router(health.router)
app.include_router(companies.router)
app.include_router(employees.router)

@app.get("/")
def root():
    return {"message": "Welcome to EnitorPay Payroll Bureau System"}
