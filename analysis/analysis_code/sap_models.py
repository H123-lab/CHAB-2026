#!/usr/bin/env python3
"""Compatibility entry point for the CHAB-2026 executable analysis pipeline.

No manuscript statistics are embedded here. The pipeline reads the locally
provided restricted adjudicator dataset and computes all results dynamically.
"""
from analysis_pipeline import main


if __name__ == "__main__":
    main()
