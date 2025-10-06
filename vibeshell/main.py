#! ./.venv/bin/python3

import argpase
from vibeshell.agent  import run_agent


def main():
    parser = argparse.ArgumentParser(description="Run VibeShell on a requirements file.")
    parser.add_argument(
        "file", nargs="?", default="requirements.vibe",
        help="Path to a .vibe file containing the requirements"
    )
    args = parser.parse_args()

    try:
        with open(args.file, "r") as f:
            requirements = f.read()
    except FileNotFoundError:
        print(f"[VibeShell] Error: '{args.file}' not found.")
        return

    print(f"[VibeShell] 🚀 Running agent on: {args.file}")
    run_agent(requirements)

    print("Hello from vibeshell!")


if __name__ == "__main__":
    main()
