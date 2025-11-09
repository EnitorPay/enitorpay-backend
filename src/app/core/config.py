import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://enitor_admin:ChingonEP8054*@enitorpay-dev.cxy80s2q2608.us-west-2.rds.amazonaws.com:5432/enitorpay"
    )

settings = Settings()
