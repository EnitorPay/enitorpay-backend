from fastapi import APIRouter
from fastapi.responses import HTMLResponse
import os
from datetime import datetime

router = APIRouter(prefix="/api/v1/aiops", tags=["AIOps"])

LOG_PATH = "/home/ssm-user/enitorpay-backend/src/logs/aiops_cron.log"


def read_log_tail(n=50):
    """Read last N lines of the AIOps log file."""
    if not os.path.exists(LOG_PATH):
        return None, "No AIOps run logs detected yet."
    try:
        with open(LOG_PATH, "r") as f:
            lines = f.readlines()[-n:]
        return lines, None
    except Exception as e:
        return None, str(e)


@router.get("/status", summary="Get latest AIOps run status")
def get_aiops_status():
    """Return the latest AIOps run summary in JSON."""
    lines, error = read_log_tail(30)
    if error:
        return {"status": "error", "message": error}
    if not lines:
        return {"status": "no_logs_found"}
    last_modified = datetime.fromtimestamp(os.path.getmtime(LOG_PATH)).isoformat()
    return {"status": "ok", "last_run": last_modified, "summary": "".join(lines)}


@router.get("/dashboard", response_class=HTMLResponse, summary="AIOps visual dashboard")
def aiops_dashboard():
    """Display a simple HTML dashboard of the latest AIOps run."""
    lines, error = read_log_tail(50)
    if error:
        return f"<h2 style='color:red;'>Error: {error}</h2>"

    if not lines:
        return "<h3>No logs available yet.</h3>"

    last_modified = datetime.fromtimestamp(os.path.getmtime(LOG_PATH)).strftime("%Y-%m-%d %H:%M:%S UTC")

    # Highlight PASS/FAIL visually
    html_lines = []
    for line in lines:
        color = "#ccc"
        if "PASS" in line:
            color = "#28a745"
        elif "FAIL" in line:
            color = "#dc3545"
        elif "INFO" in line or "Launching" in line:
            color = "#007bff"
        html_lines.append(f"<div style='color:{color}; font-family:monospace;'>{line.strip()}</div>")

    html = f"""
    <html>
    <head>
        <title>EnitorPay AIOps Dashboard</title>
        <meta charset="utf-8" />
        <style>
            body {{
                background-color: #f8f9fa;
                color: #212529;
                font-family: "Segoe UI", Tahoma, sans-serif;
                margin: 40px;
            }}
            h1 {{
                color: #2b5797;
            }}
            .container {{
                padding: 20px;
                background-color: #fff;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }}
            .timestamp {{
                font-size: 14px;
                color: #666;
                margin-bottom: 15px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>⚙️ EnitorPay AIOps Dashboard</h1>
            <div class="timestamp">Last Run: {last_modified}</div>
            <hr>
            {''.join(html_lines)}
        </div>
    </body>
    </html>
    """

    return HTMLResponse(content=html)
