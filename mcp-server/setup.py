"""
Setup script for MCP Server development environment.
Run this script to quickly set up your development environment.
"""

import sys
import subprocess
from pathlib import Path


def run_command(command: str, description: str = None) -> bool:
    """Run a shell command and return success status."""
    if description:
        print(f"🔧 {description}...")

    try:
        _ = subprocess.run(
            command, shell=True, check=True, capture_output=True, text=True
        )
        print("✅ Success")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed: {e}")
        if e.stdout:
            print(f"stdout: {e.stdout}")
        if e.stderr:
            print(f"stderr: {e.stderr}")
        return False


def main():
    """Set up the development environment."""
    print("🚀 Setting up MCP Server development environment...")

    # Check if uv is installed
    if not run_command("uv --version", "Checking if uv is installed"):
        print("Please install uv first: https://docs.astral.sh/uv/")
        sys.exit(1)

    # Install dependencies
    if not run_command("uv sync", "Installing dependencies"):
        print("Failed to install dependencies")
        sys.exit(1)

    # Create .env file if it doesn't exist
    env_file = Path(".env")
    env_example = Path(".env.example")

    if not env_file.exists() and env_example.exists():
        run_command("cp .env.example .env", "Creating .env file from example")
        print("📝 Please edit .env file with your configuration")

    # Install pre-commit hooks (if you add pre-commit later)
    # run_command("uv run pre-commit install", "Installing pre-commit hooks")

    # Run linting to check setup
    run_command("uv run ruff check .", "Running code quality checks")

    print("\n🎉 Setup complete!")
    print("\n📋 Next steps:")
    print("   1. Edit .env file with your configuration")
    print("   2. Customize mcp_server/config.yaml")
    print("   3. Start building your tools in mcp_server/server.py")
    print("   4. Run the server with: uv run python main.py")


if __name__ == "__main__":
    main()
