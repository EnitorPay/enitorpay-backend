# 🧾 EnitorPay API — v0.2.1-stable

## Overview
EnitorPay is a payroll management backend powered by **FastAPI**, **PostgreSQL**, and **AWS RDS**.
This version (v0.2.1-stable) provides live, tested endpoints for companies, employees, and payroll.

---

## Base URL
For browser and API calls:
http://34.220.246.148:8081

---

## ✅ Endpoints Summary

### 🩺 Health Check
`GET /api/v1/health/`  
**Response:**
```json
{ "status": "ok" }

[
  {
    "id": "e9fd70ef-cb07-4be9-a49c-0ce2bf74e7ea",
    "legal_name": "Enitor Test Co.",
    "dba_name": "Enitor Payroll Demo",
    "ein": "12-3456789"
  }
]
[
  {
    "id": "dc419ba7-0f1f-4f07-837b-bbd941122c97",
    "first_name": "Maria",
    "last_name": "Lopez",
    "company_id": "e9fd70ef-cb07-4be9-a49c-0ce2bf74e7ea"
  }
]
{
  "first_name": "Emily",
  "last_name": "Chen",
  "company_id": "e9fd70ef-cb07-4be9-a49c-0ce2bf74e7ea"
}
{
  "id": "generated-uuid",
  "message": "Employee created successfully"
}
[
  {
    "id": "a98f176d-cefc-4c5d-8f3f-b5937efc7529",
    "company_id": "e9fd70ef-cb07-4be9-a49c-0ce2bf74e7ea",
    "period_start": "2024-10-01",
    "period_end": "2024-10-15",
    "check_date": "2024-10-18",
    "status": "DRAFT"
  }
]
