import json
import boto3
from botocore.exceptions import BotoCoreError, ClientError

def load_rds_secret(secret_name: str = "enitorpay/rds/enitorpay-dev", region: str = "us-west-2") -> dict | None:
    try:
        sm = boto3.client("secretsmanager", region_name=region)
        resp = sm.get_secret_value(SecretId=secret_name)
        raw = resp.get("SecretString") or resp.get("SecretBinary")
        data = json.loads(raw) if isinstance(raw, str) else {}
        return {
            "host": data.get("host"),
            "port": data.get("port", 5432),
            "username": data.get("username"),
            "password": data.get("password"),
            "dbname": data.get("dbname") or data.get("database") or "enitorpay",
        }
    except (BotoCoreError, ClientError):
        return None
