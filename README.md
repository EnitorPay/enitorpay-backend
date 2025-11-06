# 💼 EnitorPay Backend — FastAPI + PostgreSQL + AWS RDS

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-RDS-blue)
![Status](https://img.shields.io/badge/Build-Stable-success)
![Version](https://img.shields.io/badge/API-v0.2.5--safe-yellow)

---

## 🚀 Overview
**EnitorPay** is a modern payroll management backend built with **FastAPI**, **SQLAlchemy**, and **AWS RDS PostgreSQL**.

This service powers the *EnitorPay Payroll Bureau System*, supporting:
- ✅ Company registry and configuration  
- ✅ Employee management (GET/POST endpoints)  
- ✅ Payroll run creation and history tracking  
- ✅ Persistent AWS RDS storage  
- ✅ Automated service startup via `systemd`

---

## 🧩 Tech Stack
| Component | Technology |
|------------|-------------|
| API Framework | FastAPI |
| ORM | SQLAlchemy |
| Database | PostgreSQL (AWS RDS) |
| Infra | AWS EC2 (Amazon Linux 2023) |
| Process Manager | systemd |
| Dependency Mgmt | Poetry |

---

## 🧠 API Endpoints

| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/api/v1/health/` | GET | Health check |
| `/api/v1/companies/` | GET | List all companies |
| `/api/v1/employees/` | GET / POST | Manage employees |
| `/api/v1/payroll/` | GET / POST | Manage pay runs |

---

## 🧰 How to Run Locally

```bash
# Install dependencies
poetry install

# Run development server
poetry run uvicorn app.main:app --app-dir src --host 127.0.0.1 --port 8081 --reload

🗃️ Database

RDS secret stored in AWS Secrets Manager under:

enitorpay/rds/enitorpay-dev

🧾 Version History
Version	Description	Date
v0.1.0-working	Initial setup & basic API health check	Oct 31, 2025
v0.2.1-stable	Employees, companies, payroll endpoints verified	Nov 2, 2025
v0.2.5-safe	Persistent RDS connection, stable service daemon	Nov 6, 2025

👨‍💻 Maintainer

Alberto De La Rosa — Enitor Inc.

“Con fuerza y visión.”
