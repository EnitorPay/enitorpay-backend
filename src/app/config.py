from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "EnitorPay"
    app_env: str = "dev"
    app_version: str = "0.1.0"

    # DB fields for now (we’ll switch to Secrets Manager next)
    db_host: str | None = None
    db_port: int = 5432
    db_name: str | None = None
    db_user: str | None = None
    db_password: str | None = None
    db_sslmode: str = "require"

    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
