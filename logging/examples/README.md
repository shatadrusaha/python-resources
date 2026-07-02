# Logging Examples

This directory contains practical examples of Python logging in action.

## Running the Examples

Each example is a standalone script. You can run them directly:

```bash
python 01_basic_logging.py
python 02_rotating_logs.py
python 03_custom_handler.py
python 04_filters.py
```

## Example Descriptions

### 01_basic_logging.py
**What it demonstrates**: Basic logging setup with `basicConfig()` and different log levels.

**Key concepts**:
- Setting up logging with `basicConfig()`
- Log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Getting a logger with `getLogger(__name__)`

**Output**: Messages displayed to console with timestamps and log levels.

---

### 02_rotating_logs.py
**What it demonstrates**: Using `RotatingFileHandler` for production log files.

**Key concepts**:
- File-based logging
- Automatic rotation when file size is exceeded
- Backup file management (`backupCount`)

**Output**: 
- Console output showing what's happening
- Multiple log files in `logs/` directory (rotating_app.log, rotating_app.log.1, etc.)

---

### 03_custom_handler.py
**What it demonstrates**: Creating a custom logging handler that stores logs in memory.

**Key concepts**:
- Extending `logging.Handler`
- Implementing `emit()` method
- Custom handlers for specialized use cases
- Retrieving specific types of logs (e.g., errors only)

**Output**:
- Console output of logs (via default handler)
- In-memory capture and analysis of logs

---

### 04_filters.py
**What it demonstrates**: Using filters to selectively log messages.

**Key concepts**:
- Creating custom filters by extending `logging.Filter`
- Filtering by log level (minimum level)
- Filtering by logger name
- Combining multiple filters

**Output**:
- Example 1: Only WARNING and above are shown
- Example 2: Only specific logger names are shown
- Example 3: Combination of filters (logger name AND level)

---

## Recommended Learning Path

1. **Start with** `01_basic_logging.py` - Understand the basics
2. **Move to** `04_filters.py` - Learn filtering
3. **Explore** `02_rotating_logs.py` - Production logging
4. **Study** `03_custom_handler.py` - Advanced customization

## Next Steps

After running these examples, try:
1. Modify the formatters in example 1
2. Change the rotation size in example 2
3. Create your own custom handler based on example 3
4. Write your own filters based on example 4

## Reference

For detailed information, see the main [README.md](../README.md) in the parent directory.
