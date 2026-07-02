#!/usr/bin/env python3
"""
Example 3: Custom Handler

Demonstrates creating a custom logging handler that stores logs in memory.
Useful for scenarios like capturing errors for reports or alerts.
Run with: python 03_custom_handler.py
"""

import logging
from datetime import datetime


class InMemoryHandler(logging.Handler):
    """
    Custom handler that stores log records in memory.
    Useful for capturing recent logs for inspection or analysis.
    """

    def __init__(self, max_records=100):
        super().__init__()
        self.records = []
        self.max_records = max_records

    def emit(self, record):
        """
        Store the formatted log record in memory.
        Remove oldest record if we exceed max_records.
        """
        formatted_record = {
            "timestamp": datetime.fromtimestamp(record.created),
            "level": record.levelname,
            "logger": record.name,
            "message": self.format(record),
            "raw_message": record.getMessage(),
        }

        self.records.append(formatted_record)

        # Remove oldest record if we exceed capacity
        if len(self.records) > self.max_records:
            self.records.pop(0)

    def get_records(self):
        """Retrieve all stored records"""
        return self.records

    def get_errors(self):
        """Get only ERROR and CRITICAL records"""
        return [r for r in self.records if r["level"] in ["ERROR", "CRITICAL"]]

    def clear(self):
        """Clear all stored records"""
        self.records.clear()


def main():
    # Setup logger
    logger = logging.getLogger("app")
    logger.setLevel(logging.DEBUG)

    # Add standard console handler
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter("%(levelname)s - %(message)s")
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # Add custom in-memory handler
    memory_handler = InMemoryHandler(max_records=50)
    memory_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    memory_handler.setFormatter(memory_formatter)
    logger.addHandler(memory_handler)

    # Log various messages
    print("=== Logging Messages ===\n")
    logger.debug("Debug information")
    logger.info("Application started")
    logger.warning("This is a warning")
    logger.error("An error occurred!")
    logger.critical("System failure!")
    logger.info("Application ended")

    # Inspect in-memory records
    print("\n=== Records in Memory ===\n")
    print(f"Total records stored: {len(memory_handler.get_records())}\n")

    print("All records:")
    for i, record in enumerate(memory_handler.get_records(), 1):
        print(f"  {i}. [{record['level']}] {record['message']}")

    print("\n\nError records only:")
    errors = memory_handler.get_errors()
    if errors:
        for error in errors:
            print(f"  [{error['level']}] {error['message']}")
    else:
        print("  No errors recorded")


if __name__ == "__main__":
    main()
