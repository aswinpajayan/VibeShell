import sys
from vibeshell.agent import run_agent

def main():
    requirements_file = "requirements.vibe"

    try:
        with open(requirements_file, "r") as f:
            requirements = f.read()
    except FileNotFoundError:
        print(f"[VibeShell] Error: '{requirements_file}' not found.")
        sys.exit(1)

    print("[VibeShell] 🚀 Starting agent...")
    run_agent(requirements)

