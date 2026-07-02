#!/usr/bin/env python3
"""
Example 4: Using Filters

Demonstrates custom filters to control which messages get logged.
Run with: python 04_filters.py
"""

import logging


class MinLevelFilter(logging.Filter):
    """Only allow messages at specified level or higher"""

    def __init__(self, level):
        super().__init__()
        self.level = level

    def filter(self, record):
        return record.levelno >= self.level


class LoggerNameFilter(logging.Filter):
    """Only allow logs from specific logger names"""

    def __init__(self, allowed_names):
        super().__init__()
        self.allowed_names = allowed_names

    def filter(self, record):
        for name in self.allowed_names:
            if record.name.startswith(name):
                return True
        return False


def example_min_level_filter():
    """Example 1: Filter by minimum level"""
    print("=== Example 1: MinLevelFilter (WARNING and above) ===\n")

    logger = logging.getLogger("example1")
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    # Add filter: only WARNING and above
    handler.addFilter(MinLevelFilter(logging.WARNING))

    logger.addHandler(handler)

    logger.debug("Debug (filtered out)")
    logger.info("Info (filtered out)")
    logger.warning("Warning (shown)")
    logger.error("Error (shown)")
    logger.critical("Critical (shown)")


def example_logger_name_filter():
    """Example 2: Filter by logger name"""
    print(
        "\n\n=== Example 2: LoggerNameFilter (only 'app.auth' and 'app.database') ===\n"
    )

    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(name)s - %(message)s")
    handler.setFormatter(formatter)
    handler.addFilter(LoggerNameFilter(["app.auth", "app.database"]))

    # Create multiple loggers
    auth_logger = logging.getLogger("app.auth")
    db_logger = logging.getLogger("app.database")
    utils_logger = logging.getLogger("app.utils")

    for logger in [auth_logger, db_logger, utils_logger]:
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)

    auth_logger.info("Auth message (shown)")
    db_logger.info("Database message (shown)")
    utils_logger.info("Utils message (filtered out)")


def example_combine_filters():
    """Example 3: Combine multiple filters"""
    print("\n\n=== Example 3: Combining Filters ===\n")
    print("Only 'app.auth' logger, ERROR level and above:\n")

    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    # Add both filters
    handler.addFilter(LoggerNameFilter(["app.auth"]))
    handler.addFilter(MinLevelFilter(logging.ERROR))

    auth_logger = logging.getLogger("app.auth")
    auth_logger.setLevel(logging.DEBUG)
    auth_logger.addHandler(handler)

    auth_logger.debug("Debug (filtered: level too low)")
    auth_logger.warning("Warning (filtered: level too low)")
    auth_logger.error("Error (shown)")
    auth_logger.critical("Critical (shown)")


if __name__ == "__main__":
    example_min_level_filter()
    example_logger_name_filter()
    example_combine_filters()
