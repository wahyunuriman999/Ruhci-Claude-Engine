# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import argparse
import sys


VERSION = "1.0.0"


def cmd_version(_args) -> None:
    print(f"Ruhci Claude Engine v{VERSION}")


def cmd_status(_args) -> None:
    try:
        from engine.core import RuhciEngine
        engine = RuhciEngine()
        health = engine.orchestrator.check_health()
        print("=== Ruhci Engine Status ===")
        for subsystem, state in health.items():
            print(f"  {subsystem:20s}: {state}")
    except Exception as e:
        print(f"Status check failed: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_run(args) -> None:
    try:
        from engine.core import RuhciEngine
        engine = RuhciEngine()
        engine.boot()
        result = engine.execute(args.objective)
        print(f"[OK] {result}")
        engine.shutdown()
    except Exception as e:
        print(f"Execution failed: {e}", file=sys.stderr)
        sys.exit(1)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ruhci",
        description="Ruhci Claude Engine — Autonomous AI Agent OS CLI",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("version", help="Print version").set_defaults(func=cmd_version)
    sub.add_parser("status", help="Print engine health").set_defaults(func=cmd_status)

    run_p = sub.add_parser("run", help="Execute an objective")
    run_p.add_argument("objective", help="High-level objective string")
    run_p.set_defaults(func=cmd_run)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
