import subprocess
import sys


def test_cli_menu():
    result = subprocess.run(
        [sys.executable, "cli.py"],
        input="8\n7\n",
        capture_output=True,
        text=True,
        timeout=5
    )

    assert "INVENTORY MANAGEMENT SYSTEM" in result.stdout
    assert "Invalid Choice" in result.stdout
    assert "Goodbye!" in result.stdout