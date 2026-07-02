#!/usr/bin/env python3
"""
Example 2: Rotating File Handler

Demonstrates log rotation based on file size.
Logs larger than 1KB will be rotated into backup files.
Run with: python 02_rotating_logs.py
"""

import logging
from logging.handlers import RotatingFileHandler
import os

# Create logs directory
os.makedirs("logs", exist_ok=True)

# Create logger
logger = logging.getLogger("rotating_example")
logger.setLevel(logging.DEBUG)

# Create RotatingFileHandler
# Rotates when file size reaches 1KB, keeps up to 3 backup files
rotating_handler = RotatingFileHandler(
    "logs/rotating_app.log",
    maxBytes=1000,  # 1 KB - rotate on small file for demo
    backupCount=3,  # Keep 3 backup files
)
rotating_handler.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
rotating_handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(rotating_handler)

# Generate logs to trigger rotation
if __name__ == "__main__":
    print("Generating logs to demonstrate rotation...")
    for i in range(50):
        logger.info(
            f"Log message {i:02d} - This is a sample entry to demonstrate log rotation"
        )

    # Show what files were created
    print("\nLog files created:")
    log_files = sorted([f for f in os.listdir("logs") if f.startswith("rotating_app")])
    for log_file in log_files:
        size = os.path.getsize(f"logs/{log_file}")
        print(f"  {log_file}: {size} bytes")

    print("\nCheck the logs/ directory to see the rotated files!")
