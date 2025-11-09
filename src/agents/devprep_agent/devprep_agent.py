import subprocess
import logging
import os
from agents.config import get_logger

log = get_logger("devprep_agent")

def check_command(cmd):
    """Run a shell command and return (success, output)."""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            log.info(f"[OK] {cmd}")
            return True, result.stdout.strip()
        else:
            log.warning(f"[FAIL] {cmd}: {result.stderr.strip()}")
            return False, result.stderr.strip()
    except Exception as e:
        log.error(f"[ERROR] running {cmd}: {e}")
        return False, str(e)

def run_dev_checks():
    log.info("Starting DevPrep Agent system checks...")

    checks = {
        "Python": "python3 --version",
        "Poetry": "poetry --version",
        "FastAPI Service": "sudo systemctl is-active enitorpay",
        "Database Connectivity": "pg_isready -h enitorpay-dev.cxy80s2q2608.us-west-2.rds.amazonaws.com -p 5432 -U enitor_admin -d enitorpay",
        "Logs Folder": "ls -ld ~/enitorpay-backend/src/logs"
    }

    results = {}
    for name, cmd in checks.items():
        success, output = check_command(cmd)
        results[name] = {"status": "PASS" if success else "FAIL", "output": output}

    log.info("DevPrep Agent completed system validation.")
    return results

if __name__ == "__main__":
    log.info("DevPrep Agent initiated locally.")
    report = run_dev_checks()
    for key, val in report.items():
        print(f"{key}: {val['status']}")
