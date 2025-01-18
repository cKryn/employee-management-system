"""
settings.py

Defines the working directory for the project, ensuring correct file path resolution
across different modules.

Modules Imported:
    - Path: Used for handling filesystem paths.
"""
from pathlib import Path

WORKDIR = Path(__file__).parent.parent