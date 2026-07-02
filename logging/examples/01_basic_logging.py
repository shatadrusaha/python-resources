#!/usr/bin/env python3
"""
Example 1: Basic Logging Setup

A simple introduction to Python logging.
Run with: python 01_basic_logging.py
"""

import logging

# Configure logging (one-time setup)
logging.basicConfig(
    level=logging.DEBUG, 
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Get a logger
logger = logging.getLogger(__name__)

# Log at different levels
if __name__ == "__main__":
    logger.debug("Debug message - detailed diagnostic info")
    logger.info("Info message - general informational message")
    logger.warning("Warning message - something unexpected happened")
    logger.error("Error message - a serious problem occurred")
    logger.critical("Critical message - system failure imminent")
