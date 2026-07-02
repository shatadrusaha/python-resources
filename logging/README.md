# Python Logging Module: Quick Reference Guide

**A comprehensive guide to the Python `logging` module for beginners and intermediate developers.**

---

## Table of Contents

1. [What is Logging?](#what-is-logging)
2. [Core Concepts](#core-concepts)
3. [Log Levels](#log-levels)
4. [Quick Start](#quick-start)
5. [Configuration Approaches](#configuration-approaches)
6. [Handlers - Where Logs Go](#handlers)
7. [Formatters - Formatting Output](#formatters)
8. [Filters - Selective Logging](#filters)
9. [Common Patterns](#common-patterns)
10. [Best Practices](#best-practices)
11. [Common Pitfalls](#common-pitfalls)
12. [Quick Reference Table](#quick-reference)
13. [Copy-Paste Examples](#copy-paste-examples)

---

## What is Logging?

### The Problem: Print Statements Are Not Enough

```python
# ❌ Bad: Using print statements
print("Starting process")
print("User authenticated")
print("Error: Connection failed")
print("Process complete")
```

**Problems:**
- No timestamps → Can't tell when events happened
- No severity levels → Can't distinguish between info and errors
- Can't be disabled at runtime → Clutters output
- Goes everywhere → No control over destination
- Not suitable for production → Hard to filter and analyze

### The Solution: Professional Logging

```python
# ✅ Good: Using logging module
import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

logger.debug("Starting process")
logger.info("User authenticated")
logger.error("Error: Connection failed")
logger.info("Process complete")
```

**Advantages:**
- **Timestamps** - Know exactly when events occurred
- **Severity levels** - DEBUG, INFO, WARNING, ERROR, CRITICAL
- **Configurable** - Change behavior at runtime without code changes
- **Flexible output** - Send to console, files, email, Slack, databases, etc.
- **Structured** - Consistent format across entire application
- **Production-ready** - Built into Python standard library

---

## Core Concepts

### The Four Main Components

```
┌─────────────────────────────────────────────┐
│ Your Code                                    │
│ logger.info("Something happened")           │
└────────────────┬────────────────────────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ Logger          │ Creates LogRecord
        │ (e.g., root)    │
        └────────┬────────┘
                 │
        ┌────────▼────────┐
        │ Filter (opt)    │ Decides if to process
        └────────┬────────┘
                 │
    ┌────────────▼──────────────┐
    │ Handler                   │
    │ (FileHandler, console)    │ Sends somewhere
    └────────┬──────────────────┘
             │
    ┌────────▼──────────────┐
    │ Formatter (opt)       │ Formats message
    └────────┬──────────────┘
             │
             ▼
      Output destination
     (file, console, etc)
```

### Component Definitions

| Component | Purpose | Example |
|-----------|---------|---------|
| **Logger** | Interface you use to log messages | `logging.getLogger('app.database')` |
| **Handler** | Sends logs to a destination | `FileHandler`, `StreamHandler`, `RotatingFileHandler` |
| **Formatter** | Controls log message format | `'%(asctime)s - %(levelname)s - %(message)s'` |
| **Filter** | Decides which records to log | `logging.Filter` (custom class) |
| **LogRecord** | Individual log entry | Created automatically by logger |

### Logger Hierarchy

Loggers form a hierarchy using dot notation:

```
root
├── app
│   ├── app.auth
│   ├── app.database
│   │   ├── app.database.connection
│   │   └── app.database.query
│   └── app.api
└── library
    └── library.utils
```

**Key Properties:**
- Child loggers inherit settings from parents (unless overridden)
- Use `logger.setLevel()` to override parent level
- Use `logger.propagate = False` to stop propagation up the hierarchy

---

## Log Levels

| Level | Value | Use Case | When to Use |
|-------|-------|----------|------------|
| **DEBUG** | 10 | Detailed diagnostic info for developers | Variable values, function entry/exit, loops |
| **INFO** | 20 | General information about application flow | Application started, user action, milestone reached |
| **WARNING** | 30 | Warning about potential issues (default level) | Deprecated feature, performance degradation |
| **ERROR** | 40 | Error - something went wrong, functionality broken | Exception caught, operation failed |
| **CRITICAL** | 50 | Critical error - system may not continue | System out of memory, fatal error |
| **NOTSET** | 0 | No level set (inherit from parent) | Rarely used directly |

### Log Level Filtering

Only messages at the configured level or higher are logged:

```
Configured Level: WARNING
┌──────────────────────────────┐
│ DEBUG    ❌ FILTERED OUT      │
│ INFO     ❌ FILTERED OUT      │
│ WARNING  ✅ LOGGED            │
│ ERROR    ✅ LOGGED            │
│ CRITICAL ✅ LOGGED            │
└──────────────────────────────┘
```

---

## Quick Start

### The Simplest Way: basicConfig()

```python
import logging

# Configure logging (do this ONCE, early in your program)
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Get a logger
logger = logging.getLogger(__name__)

# Start logging
logger.debug("Debug message")
logger.info("Info message")
logger.error("Error message")
```

**Important:** `basicConfig()` only works BEFORE creating loggers. Call it first!

### Common basicConfig Parameters

```python
logging.basicConfig(
    level=logging.DEBUG,  # Minimum level to capture
    format="%(message)s",  # Message format (see Formatters section)
    filename="app.log",  # File to write to (default: stderr)
    filemode="a",  # 'a' = append, 'w' = overwrite
    datefmt="%Y-%m-%d %H:%M:%S",  # Date format
    encoding="utf-8",  # File encoding
)
```

---

## Configuration Approaches

### 1. basicConfig() - Simple, One-Time Setup

**Best for:** Small scripts, quick prototypes

```python
import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
logger.info("Application started")
```

**Limitations:**
- Only one handler
- Limited customization
- Runs only once

---

### 2. Dictionary Configuration (dictConfig) - Flexible, Recommended

**Best for:** Medium to large applications, multiple handlers/loggers

```python
import logging.config

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"}
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "standard",
            "stream": "ext://sys.stdout",
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "standard",
            "filename": "app.log",
        },
    },
    "loggers": {
        "app": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
        }
    },
}

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("app")
logger.info("Application started")
```

---

### 3. INI File Configuration - Externalize Settings

**Best for:** Production systems, configuration management

**Create `logging.conf`:**
```ini
[loggers]
keys=root,app

[handlers]
keys=console,file

[formatters]
keys=standard

[logger_root]
level=DEBUG
handlers=console

[logger_app]
level=DEBUG
handlers=file
qualname=app
propagate=0

[handler_console]
class=StreamHandler
level=INFO
formatter=standard
args=(sys.stdout,)

[handler_file]
class=FileHandler
level=DEBUG
formatter=standard
args=('app.log',)

[formatter_standard]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
```

**Load configuration:**
```python
import logging.config

logging.config.fileConfig("logging.conf")
logger = logging.getLogger("app")
logger.info("Application started")
```

---

## Handlers

### What Handlers Do

Handlers control WHERE logs go:
- **StreamHandler** → Console (stdout/stderr)
- **FileHandler** → Single file
- **RotatingFileHandler** → Multiple files with rotation by size
- **TimedRotatingFileHandler** → Multiple files with rotation by time
- **NullHandler** → Discard logs (use in libraries)
- Custom handlers → Email, Slack, database, etc.

### Common Handlers

#### StreamHandler (Console Output)

```python
import logging
import sys

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

# Output to stdout
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.info("Message to console")
```

#### FileHandler (Single File)

```python
import logging

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler("app.log")
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.info("Message written to app.log")
```

#### RotatingFileHandler (Size-Based Rotation)

```python
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

# Rotate when file reaches 1MB, keep 5 backups
handler = RotatingFileHandler(
    "app.log",
    maxBytes=1024 * 1024,  # 1MB
    backupCount=5,  # Keep app.log.1, app.log.2, etc.
)
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

# Generate logs
for i in range(1000):
    logger.info(f"Message {i}")
```

#### TimedRotatingFileHandler (Time-Based Rotation)

```python
import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

# Rotate daily at midnight, keep 7 days
handler = TimedRotatingFileHandler(
    "app.log",
    when="midnight",  # Rotate at midnight
    interval=1,  # Every 1 day
    backupCount=7,  # Keep 7 days of logs
)
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.info("Daily rotation configured")
```

---

## Formatters

### Format Attributes

The format string controls what information appears in each log message:

| Attribute | Description | Example |
|-----------|-------------|---------|
| `%(name)s` | Logger name | `app.database` |
| `%(levelname)s` | Log level | `INFO`, `ERROR` |
| `%(message)s` | The log message | `User authenticated` |
| `%(asctime)s` | Timestamp | `2024-06-04 10:30:45,123` |
| `%(filename)s` | Source filename | `app.py` |
| `%(lineno)d` | Line number | `42` |
| `%(funcName)s` | Function name | `authenticate_user` |
| `%(pathname)s` | Full file path | `/app/auth.py` |
| `%(process)d` | Process ID | `12345` |
| `%(thread)d` | Thread ID | `139876543210` |
| `%(msecs)d` | Milliseconds | `123` |

### Common Format Strings

```python
# Simple
"%(levelname)s - %(message)s"

# With timestamp
"%(asctime)s - %(levelname)s - %(message)s"

# With logger name
"%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Detailed (with file/line info)
"[%(asctime)s] %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s"

# Very detailed (with function info)
"%(asctime)s - %(name)s - %(levelname)s - [%(funcName)s] %(message)s"

# JSON-like
"%(asctime)s | %(name)s | %(levelname)s | %(message)s | %(filename)s:%(lineno)d"
```

### Custom Timestamp Format

```python
import logging

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",  # Custom date format
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger("app")
logger.addHandler(handler)
logger.info("Message with custom timestamp")
```

---

## Filters

### What Filters Do

Filters allow selective logging based on custom logic:

```python
import logging


class MinLevelFilter(logging.Filter):
    """Only allow messages at specified level or higher"""

    def __init__(self, level):
        super().__init__()
        self.level = level

    def filter(self, record):
        return record.levelno >= self.level


logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.addFilter(MinLevelFilter(logging.WARNING))
logger.addHandler(handler)

logger.debug("Debug (filtered)")  # Not shown
logger.info("Info (filtered)")  # Not shown
logger.warning("Warning (shown)")  # Shown
logger.error("Error (shown)")  # Shown
```

### Filter by Logger Name

```python
import logging


class LoggerNameFilter(logging.Filter):
    """Only allow specific logger names"""

    def __init__(self, allowed_names):
        super().__init__()
        self.allowed_names = allowed_names

    def filter(self, record):
        return any(record.name.startswith(name) for name in self.allowed_names)


# Usage
handler = logging.StreamHandler()
handler.addFilter(LoggerNameFilter(["app.auth", "app.database"]))
logger.addHandler(handler)
```

### Filter Sensitive Information

```python
import logging
import re


class SensitiveInfoFilter(logging.Filter):
    """Remove sensitive data from logs"""

    def filter(self, record):
        # Mask email addresses
        record.msg = re.sub(r"[\w.-]+@[\w.-]+", "[EMAIL_HIDDEN]", str(record.msg))
        # Mask API keys
        record.msg = re.sub(
            r"api[_-]?key[:\s=]*\S+", "[API_KEY_HIDDEN]", str(record.msg)
        )
        return True


handler = logging.StreamHandler()
handler.addFilter(SensitiveInfoFilter())
logger.addHandler(handler)
```

---

## Common Patterns

### Pattern 1: Per-Module Logging

**In each module, use `__name__`:**

```python
# module_a.py
import logging

logger = logging.getLogger(__name__)


def do_something():
    logger.debug("Starting task")
    logger.info("Task completed")
```

**Configure at application startup:**

```python
# main.py
import logging.config

logging.basicConfig(level=logging.DEBUG)

import module_a

module_a.do_something()
```

### Pattern 2: Separate Handlers for Different Log Levels

```python
import logging

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

# Console: only WARNING and above (brief)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
console_formatter = logging.Formatter("%(levelname)s - %(message)s")
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

# File: everything (verbose)
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

logger.debug("Debug (file only)")
logger.warning("Warning (console + file)")
```

### Pattern 3: Library Logging (NullHandler)

**In libraries, don't configure logging. Let the application handle it:**

```python
# my_library/__init__.py
import logging

# NullHandler prevents "No handlers found" warning
logging.getLogger(__name__).addHandler(logging.NullHandler())

logger = logging.getLogger(__name__)


def some_function():
    logger.info("Doing something")
```

### Pattern 4: Context Information

```python
import logging
from functools import wraps


def log_context(logger, **context):
    """Add context to all logs in a block"""

    class ContextFilter(logging.Filter):
        def filter(self, record):
            for key, value in context.items():
                setattr(record, key, value)
            return True

    handler = logging.StreamHandler()
    handler.addFilter(ContextFilter())
    formatter = logging.Formatter("%(request_id)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)


logger = logging.getLogger("app")

# Usage
logger.info("Processing", extra={"request_id": "REQ-123"})
```

---

## Best Practices

### ✅ Do's

1. **Configure logging once at startup**
   ```python
   # In main.py or __init__.py
   logging.basicConfig(...)
   ```

2. **Use `__name__` for logger name**
   ```python
   logger = logging.getLogger(__name__)  # Matches module name
   ```

3. **Use appropriate log levels**
   - DEBUG: Development diagnostics
   - INFO: Application flow (users started, requests processed)
   - WARNING: Unexpected but recoverable situations
   - ERROR: Errors that need attention
   - CRITICAL: System failure

4. **Include context in error logs**
   ```python
   logger.error("Failed to process user", extra={"user_id": user_id})
   ```

5. **Use `exc_info=True` for exceptions**
   ```python
   try:
       risky_operation()
   except Exception:
       logger.error("Operation failed", exc_info=True)  # Includes traceback
   ```

6. **Use rotating file handlers for production**
   ```python
   from logging.handlers import RotatingFileHandler

   handler = RotatingFileHandler("app.log", maxBytes=1024 * 1024, backupCount=5)
   ```

7. **Mask sensitive information**
   ```python
   logger.info(f"User: {username}, ID: {user_id[-4:]}***")  # Mask secrets
   ```

### ❌ Don'ts

1. **Don't hardcode configuration in libraries**
   ```python
   # ❌ Bad: In library code
   logging.basicConfig(...)
   
   # ✅ Good: Let the application configure
   logger = logging.getLogger(__name__)
   logger.addHandler(logging.NullHandler())
   ```

2. **Don't log passwords, API keys, or tokens**
   ```python
   # ❌ Bad
   logger.info(f"API key: {api_key}")
   
   # ✅ Good
   logger.info("API authenticated successfully")
   ```

3. **Don't use string formatting in log messages**
   ```python
   # ❌ Bad: String interpolation happens before logging
   logger.info(f"User {user.name} did {action}")
   
   # ✅ Good: Let logging handle formatting
   logger.info("User %s did %s", user.name, action)
   ```

4. **Don't call `basicConfig()` multiple times**
   ```python
   # ❌ Bad
   logging.basicConfig(...)
   logging.basicConfig(...)  # Second call is ignored
   
   # ✅ Good: Call once at startup
   logging.basicConfig(...)
   ```

5. **Don't over-log at INFO level**
   ```python
   # ❌ Bad: Too much noise
   logger.info(f"Loop iteration {i}")
   
   # ✅ Good: Use DEBUG for detailed info
   logger.debug(f"Loop iteration {i}")
   ```

---

## Common Pitfalls

### Pitfall 1: String Interpolation Performance

```python
# ❌ Bad: String is formatted even if not logged
logger.debug(f"Value: {expensive_function()}")  # expensive_function() called always

# ✅ Good: Formatting only if level is enabled
logger.debug(
    "Value: %s", expensive_function()
)  # expensive_function() only if DEBUG enabled
```

### Pitfall 2: Handler Conflicts

```python
# ❌ Bad: Multiple configurations conflict
logging.basicConfig(level=logging.DEBUG)  # First config
logging.basicConfig(level=logging.WARNING)  # Second config ignored!

# ✅ Good: One configuration
logging.basicConfig(level=logging.DEBUG)
```

### Pitfall 3: Thread Safety Issues

```python
# ⚠️  Note: logging module IS thread-safe
# But if you create custom handlers, ensure they're thread-safe
```

### Pitfall 4: Module Import Order

```python
# ❌ Bad: Logger configured after imports
import module_a

logging.basicConfig(...)  # Too late

# ✅ Good: Configure first, then import
logging.basicConfig(...)
import module_a
```

### Pitfall 5: Logger Propagation Confusion

```python
# ❌ Bad: Message logged twice (parent + child handlers)
root = logging.getLogger()
app = logging.getLogger("app")
root.addHandler(handler1)
app.addHandler(handler2)
app.info("Message")  # Goes to both handlers!

# ✅ Good: Disable propagation if needed
app.propagate = False
```

---

## Quick Reference

### Logger Methods

| Method | Use | Example |
|--------|-----|---------|
| `logger.debug()` | Diagnostic info | `logger.debug("Variable x = %s", x)` |
| `logger.info()` | General info | `logger.info("Request received")` |
| `logger.warning()` | Warning (default level) | `logger.warning("Deprecated API")` |
| `logger.error()` | Error | `logger.error("Failed to connect")` |
| `logger.critical()` | Critical | `logger.critical("Out of memory")` |
| `logger.exception()` | Error with traceback | `logger.exception("Operation failed")` |
| `logger.setLevel()` | Change level | `logger.setLevel(logging.DEBUG)` |
| `logger.addHandler()` | Add handler | `logger.addHandler(handler)` |
| `logger.addFilter()` | Add filter | `logger.addFilter(filter)` |

### Handler Types

| Handler | Purpose | Parameters |
|---------|---------|------------|
| `StreamHandler` | Console output | `stream=sys.stdout` |
| `FileHandler` | File output | `filename='app.log'` |
| `RotatingFileHandler` | Rotate by size | `maxBytes=1024*1024, backupCount=5` |
| `TimedRotatingFileHandler` | Rotate by time | `when='midnight', backupCount=7` |
| `NullHandler` | Discard logs | (no params) |
| `MemoryHandler` | Buffer in memory | `capacity=100` |
| `QueueHandler` | Non-blocking (async) | `queue=log_queue` |

### Level Constants

```python
logging.DEBUG  # 10 - Diagnostic info
logging.INFO  # 20 - General information
logging.WARNING  # 30 - Warnings (default)
logging.ERROR  # 40 - Errors
logging.CRITICAL  # 50 - Critical failures
```

---

## Copy-Paste Examples

### Example 1: Simple Application Logging

```python
import logging

# One-time setup
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# In your modules
logger = logging.getLogger(__name__)


def main():
    logger.info("Application started")
    logger.debug("Debug information")
    logger.error("An error occurred")


if __name__ == "__main__":
    main()
```

### Example 2: Console + File Logging

```python
import logging

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter("%(levelname)s - %(message)s")
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

# File handler
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# Usage
logger.debug("Debug info (file only)")
logger.info("Information (console + file)")
logger.error("Error (console + file)")
```

### Example 3: Rotating File Handler

```python
import logging
from logging.handlers import RotatingFileHandler
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

handler = RotatingFileHandler(
    "logs/app.log",
    maxBytes=5 * 1024 * 1024,  # 5MB
    backupCount=5,
)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Application started with rotating logs")
```

### Example 4: Dictionary Configuration

```python
import logging
import logging.config

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "standard",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "app": {
            "level": "DEBUG",
            "handlers": ["console"],
        }
    },
}

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("app")
logger.info("Application started")
```

### Example 5: Exception Logging

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

try:
    result = 1 / 0
except ZeroDivisionError:
    # Option 1: Use exc_info=True
    logger.error("Math error occurred", exc_info=True)
    
    # Option 2: Use exception() shortcut (same as above)
    # logger.exception("Math error occurred")
```

### Example 6: Custom Filter

```python
import logging


class SensitiveDataFilter(logging.Filter):
    def filter(self, record):
        # Hide email addresses
        record.msg = str(record.msg).replace("@", "[AT]")
        return True


logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.addFilter(SensitiveDataFilter())
formatter = logging.Formatter("%(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Contact user@example.com")  # Output: Contact user[AT]example.com
```

---

## Further Reading

- **Official Documentation**: https://docs.python.org/3/library/logging.html
- **Logging Cookbook**: https://docs.python.org/3/library/logging.cookbook.html
- **Best Practices**: https://docs.python.org/3/library/logging.html#logging-best-practices

---

## Summary

- **Use logging** instead of print statements in production
- **Configure once** at application startup
- **Use appropriate levels** (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- **Multiple handlers** for different outputs and levels
- **Formatters** to control message format
- **Filters** to selectively log
- **Rotating handlers** for log files in production
- **Never log secrets** - mask sensitive information
- **Use `__name__`** for logger names in modules

Happy logging! 🎯
