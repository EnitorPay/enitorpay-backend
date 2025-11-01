from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import os
import boto3
import json

# Retrieve the PostgreSQL connection info from AWS Secrets Manager
def build_dsn() -> str:
    secret_name = os.getenv("ENITORPAY_DB_SECRET", "enitorpay/rds/enitorpay-dev")
    region_name = os.getenv("AWS_REGION", "us-west-2")

    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region_name)
    get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    secret = json.loads(get_secret_value_response["SecretString"])

    # Build a DSN string
    return (
        f"postgresql+psycopg2://{secret['username']}:{secret['password']}"
        f"@{secret['host']}:{secret['port']}/{secret['dbname']}"
    )

# Create SQLAlchemy engine and session factory
def get_engine():
    engine = create_engine(build_dsn(), pool_pre_ping=True)
    return engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=get_engine())

# ✅ Dependency for FastAPI
def get_session() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
