#!/usr/bin/env python3
"""Compatibility entry point for the CHAB-2026 executable analysis pipeline.

No manuscript statistics are embedded here. The pipeline reads the locally
provided restricted adjudicator dataset and computes all results dynamically.
"""
from pathlib import Path
import sys

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from analysis_pipeline import main


if __name__ == "__main__":
    main()
