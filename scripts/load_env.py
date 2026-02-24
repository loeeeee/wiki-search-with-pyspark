#!/usr/bin/env python3
"""
Environment variable loader for nix shell.

This script loads environment variables from env.yaml and outputs
export commands for the shell to evaluate.
"""

import logging
import os
import sys
from pathlib import Path

import yaml

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)

# Default environment variables
DEFAULT_ENV = {
    "DEBUG": "false",
    "SECRET_KEY": "default-dev-key-change-in-production",
    "DATABASE_URL": "sqlite:///db.sqlite3",
    "LOG_LEVEL": "INFO",
    "PYTHON_ENV": "development",
}

ENV_FILE = Path("env.yaml")


def create_default_env_file() -> None:
    """Create env.yaml with default values if it does not exist."""
    if ENV_FILE.exists():
        return

    logger.info("Creating %s with default values", ENV_FILE)
    with open(ENV_FILE, "w", encoding="utf-8") as f:
        yaml.dump(DEFAULT_ENV, f, default_flow_style=False, sort_keys=True)
    logger.info("Created %s", ENV_FILE)


def load_env_file() -> dict[str, str]:
    """Load environment variables from env.yaml.

    Returns:
        Dictionary of environment variable names and values.
    """
    with open(ENV_FILE, encoding="utf-8") as f:
        env_vars = yaml.safe_load(f)

    if env_vars is None:
        return {}

    # Convert all values to strings
    return {str(k): str(v) for k, v in env_vars.items()}


def export_variables(env_vars: dict[str, str]) -> None:
    """Output export commands for shell evaluation.

    Args:
        env_vars: Dictionary of environment variables to export.
    """
    for key, value in env_vars.items():
        # Escape single quotes in value
        escaped_value = value.replace("'", "'\"'\"'")
        print(f"export {key}='{escaped_value}'")


def main() -> int:
    """Main entry point.

    Returns:
        Exit code (0 for success, 1 for error).
    """
    try:
        # Create default env file if it doesn't exist
        create_default_env_file()

        # Load environment variables
        env_vars = load_env_file()

        # Output export commands
        export_variables(env_vars)

        logger.info("Loaded %d environment variables from %s", len(env_vars), ENV_FILE)
        return 0

    except FileNotFoundError:
        logger.error("%s not found and could not be created", ENV_FILE)
        return 1
    except yaml.YAMLError as e:
        logger.error("Invalid YAML in %s: %s", ENV_FILE, e)
        return 1
    except Exception as e:
        logger.error("Failed to load environment: %s", e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
