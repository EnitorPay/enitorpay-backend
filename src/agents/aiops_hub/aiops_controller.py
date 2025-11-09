import argparse
import importlib
import logging
import os
import sys
from pathlib import Path

# === Logging setup ===
LOG_DIR = Path(__file__).resolve().parent.parent / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "aiops_hub.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [AI-Ops Hub] %(message)s",
)
log = logging.getLogger("aiops_hub")

# === Dynamic Agent Loader ===
AGENTS_DIR = Path(__file__).resolve().parent.parent
AVAILABLE_AGENTS = {}

for agent_dir in AGENTS_DIR.iterdir():
    agent_name = agent_dir.name
    entry_file = agent_dir / f"{agent_name}.py"
    if entry_file.exists():
        AVAILABLE_AGENTS[agent_name] = entry_file

def run_agent(name: str, *args):
    """Run a specific agent module dynamically."""
    try:
        if name not in AVAILABLE_AGENTS:
            print(f"⚠️  Agent '{name}' not found.")
            log.warning(f"Agent '{name}' not found.")
            return
        module_path = f"agents.{name}.{name}"
        module = importlib.import_module(module_path)
        log.info(f"Executing agent: {name}")
        if hasattr(module, "lambda_handler"):
            result = module.lambda_handler({"topic": "AI-Ops orchestration"}, None)
            print(result)
        elif hasattr(module, "run_dev_checks"):
            result = module.run_dev_checks()
            print(result)
        else:
            print(f"Agent '{name}' loaded but no known entry function found.")
    except Exception as e:
        log.error(f"Error executing {name}: {e}")
        print(f"❌ Error executing {name}: {e}")

def run_all():
    """Run all detected agents sequentially."""
    print("🚀 Running all agents...\n")
    for agent in AVAILABLE_AGENTS:
        print(f"▶️  Launching {agent}...")
        run_agent(agent)
        print("-" * 40)
    print("✅ All agents completed.")

# === CLI Interface ===
def main():
    parser = argparse.ArgumentParser(description="EnitorPay AI-Ops Control Hub")
    parser.add_argument("action", choices=["list", "run", "full"], help="Action to perform")
    parser.add_argument("agent", nargs="?", help="Agent name (for 'run')")
    args = parser.parse_args()

    if args.action == "list":
        print("🧩 Available agents:")
        for name in AVAILABLE_AGENTS:
            print(f" - {name}")
    elif args.action == "run" and args.agent:
        run_agent(args.agent)
    elif args.action == "full":
        run_all()
    else:
        parser.print_help()

if __name__ == "__main__":
    log.info("AI-Ops Hub started.")
    main()
