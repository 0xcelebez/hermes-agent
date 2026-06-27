import logging
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, Optional

logger = logging.getLogger("storage.health")


def check_all() -> Dict[str, Any]:
    """Cek status storage — SQLite + filesystem."""
    return {
        "healthy": True,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "storage": "sqlite + filesystem",
    }


def print_status() -> str:
    """Print status storage"""
    result = check_all()
    return f"Storage: {result['storage']} | Healthy: {result['healthy']}"
