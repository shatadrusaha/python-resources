# PySpark Comprehensive Tutorial

A complete guide to Apache Spark with Python — from fundamentals to advanced techniques.

## Table of Contents

- [What is PySpark?](#what-is-pyspark)
- [Architecture Overview](#architecture-overview)
- [Installation & Setup](#installation--setup)
- [Core Concepts](#core-concepts)
- [Quick Reference](#quick-reference)
- [Performance Best Practices](#performance-best-practices)
- [Resources](#resources)

---

## What is PySpark?

PySpark is the Python API for Apache Spark — a distributed computing framework designed for large-scale data processing. It provides:

- **Speed**: In-memory computation, up to 100x faster than Hadoop MapReduce
- **Unified Engine**: Batch processing, streaming, SQL, ML, and graph computation
- **Ease of Use**: High-level APIs in Python, Scala, Java, R
- **Scalability**: From a single laptop to thousands of nodes

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────┐
│                   Driver Program                     │
│  ┌───────────────────────────────────────────────┐  │
│  │              SparkSession                      │  │
│  │  (Entry point: combines SparkContext,          │  │
│  │   SQLContext, HiveContext)                     │  │
│  └───────────────────────────────────────────────┘  │
└──────────────────────┬──────────────────────────────┘
                       │
              ┌────────▼────────┐
              │  Cluster Manager │
              │  (Local/YARN/    │
              │   Mesos/K8s)    │
              └────────┬────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
   ┌────▼────┐   ┌────▼────┐   ┌────▼────┐
   │ Worker  │   │ Worker  │   │ Worker  │
   │  Node   │   │  Node   │   │  Node   │
   │         │   │         │   │         │
   │┌───────┐│   │┌───────┐│   │┌───────┐│
   ││Executor││   ││Executor││   ││Executor││
   │├───────┤│   │├───────┤│   │├───────┤│
   ││ Tasks  ││   ││ Tasks  ││   ││ Tasks  ││
   │└───────┘│   │└───────┘│   │└───────┘│
   └─────────┘   └─────────┘   └─────────┘
```

### Key Components

| Component | Description |
|-----------|-------------|
| **SparkSession** | Unified entry point for all Spark functionality |
| **Driver** | Process that runs the main program and creates SparkSession |
| **Executor** | Process on worker nodes that runs tasks and stores data |
| **Task** | Unit of work sent to an executor |
| **Partition** | Logical chunk of data distributed across the cluster |
| **DAG** | Directed Acyclic Graph — execution plan of transformations |

### Lazy Evaluation

Spark uses **lazy evaluation** — transformations are not executed immediately. Instead, Spark builds a DAG of transformations and only executes when an **action** is called.

```
Transformations (lazy)          Actions (trigger execution)
─────────────────────           ──────────────────────────
select()                        show()
filter() / where()              count()
groupBy()                       collect()
join()                          write()
withColumn()                    first() / head()
orderBy() / sort()              take()
distinct()                      toPandas()
```

---

## Installation & Setup

### Prerequisites

- Python 3.9+
- Java 17 (OpenJDK recommended — LTS, supported by PySpark 3.4+)

### Install Java (macOS)

```bash
brew install openjdk@17
# Add to PATH (add to ~/.zshrc for persistence)
export JAVA_HOME=$(/usr/libexec/java_home -v 17)
```

### Install PySpark

```bash
# Using uv (recommended for this project)
uv add pyspark

# Or with pip
pip install pyspark
```

### Verify Installation

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").appName("test").getOrCreate()

print(spark.version)
spark.stop()
```

### Configuration Options

```python
spark = SparkSession.builder \
    .master("local[*]") \                    # Use all available cores
    .appName("MyApp") \
    .config("spark.sql.shuffle.partitions", "8") \  # Reduce for local
    .config("spark.driver.memory", "4g") \
    .config("spark.executor.memory", "4g") \
    .config("spark.sql.adaptive.enabled", "true") \  # Adaptive query execution
    .getOrCreate()
```

---

## Core Concepts

### DataFrame vs RDD

| Feature | DataFrame | RDD |
|---------|-----------|-----|
| Abstraction | Distributed table with named columns | Distributed collection of objects |
| Optimization | Catalyst optimizer + Tungsten engine | No automatic optimization |
| Schema | Yes (typed columns) | No schema |
| API | SQL-like (select, filter, groupBy) | Functional (map, filter, reduce) |
| Performance | Faster (optimized execution plans) | Slower (no optimization) |
| Use Case | Structured/semi-structured data | Unstructured data, fine-grained control |

**Recommendation**: Use DataFrames for 95% of use cases.

### Transformations vs Actions

**Narrow Transformations** — each input partition contributes to at most one output partition:
- `select()`, `filter()`, `withColumn()`, `map()`

**Wide Transformations** — input partitions contribute to multiple output partitions (require shuffle):
- `groupBy()`, `join()`, `orderBy()`, `distinct()`, `repartition()`

### Data Types

```python
from pyspark.sql.types import *

# Common types
StringType()  # String
IntegerType()  # 32-bit integer
LongType()  # 64-bit integer
FloatType()  # 32-bit float
DoubleType()  # 64-bit float
BooleanType()  # Boolean
DateType()  # Date
TimestampType()  # Timestamp
ArrayType(T)  # Array of type T
MapType(K, V)  # Map with key K and value V
StructType([...])  # Nested structure (row)
```

---

## Quick Reference

### Reading Data

```python
# CSV
df = spark.read.csv("path/to/file.csv", header=True, inferSchema=True)

# Parquet (preferred format)
df = spark.read.parquet("path/to/file.parquet")

# JSON
df = spark.read.json("path/to/file.json")

# JDBC
df = spark.read.jdbc(url, table, properties={"user": "u", "password": "p"})
```

### Writing Data

```python
# Parquet (default, columnar, compressed)
df.write.parquet("output/path")

# CSV
df.write.csv("output/path", header=True)

# Partitioned write
df.write.partitionBy("year", "month").parquet("output/path")

# Write modes: overwrite, append, ignore, error (default)
df.write.mode("overwrite").parquet("output/path")
```

### DataFrame Operations

```python
# Selection
df.select("col1", "col2")
df.select(col("col1").alias("new_name"))

# Filtering
df.filter(col("age") > 25)
df.where((col("age") > 25) & (col("city") == "NYC"))

# Adding/Modifying columns
df.withColumn("new_col", col("price") * 1.1)
df.withColumnRenamed("old_name", "new_name")

# Aggregation
df.groupBy("department").agg(
    count("*").alias("total"),
    avg("salary").alias("avg_salary"),
    max("salary").alias("max_salary"),
)

# Sorting
df.orderBy(col("salary").desc())

# Joins
df1.join(df2, df1["id"] == df2["id"], "inner")  # inner, left, right, full, cross

# Window Functions
from pyspark.sql.window import Window

window = Window.partitionBy("dept").orderBy(col("salary").desc())
df.withColumn("rank", rank().over(window))

# Distinct & Drop Duplicates
df.distinct()
df.dropDuplicates(["col1", "col2"])
```

### Spark SQL

```python
df.createOrReplaceTempView("employees")
result = spark.sql("""
    SELECT department, AVG(salary) as avg_salary
    FROM employees
    GROUP BY department
    HAVING AVG(salary) > 50000
""")
```

---

## Performance Best Practices

### 1. Partitioning

```python
# Repartition (full shuffle — use for increasing partitions)
df.repartition(200)
df.repartition("key_column")  # Hash partition by column

# Coalesce (no shuffle — use for reducing partitions)
df.coalesce(4)
```

**Rule of thumb**: 2-4 partitions per CPU core, ~128MB per partition.

### 2. Caching

```python
# Cache frequently used DataFrames
df.cache()  # MEMORY_AND_DISK (default)
df.persist(StorageLevel.MEMORY_ONLY)
df.unpersist()  # Release cache
```

### 3. Broadcast Joins

```python
from pyspark.sql.functions import broadcast

# Use when one table is small (< 10MB default threshold)
large_df.join(broadcast(small_df), "key")
```

### 4. Avoid These Anti-Patterns

| Anti-Pattern | Better Alternative |
|---|---|
| `collect()` on large data | Use `take(n)` or `show(n)` |
| Python UDFs | Use built-in functions or Pandas UDFs |
| `for` loops over rows | Use DataFrame transformations |
| Too many small files | `coalesce()` before writing |
| `count()` just to check emptiness | Use `df.head(1)` or `df.isEmpty()` |
| Repeated joins on same key | Pre-partition with `repartition(key)` |

### 5. Adaptive Query Execution (AQE)

```python
# Enable AQE (default in Spark 3.2+)
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")
```

### 6. Monitoring

```python
# Explain query plan
df.explain(True)  # Physical + Logical plan
df.explain("cost")  # With cost estimates

# Spark UI (available at localhost:4040 during session)
```

---

## Resources

### Official Documentation
- [PySpark Documentation](https://spark.apache.org/docs/latest/api/python/)
- [Spark SQL Guide](https://spark.apache.org/docs/latest/sql-programming-guide.html)
- [Structured Streaming](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html)

### Books
- *Learning Spark, 2nd Edition* — Jules Damji et al. (O'Reilly)
- *Spark: The Definitive Guide* — Bill Chambers & Matei Zaharia (O'Reilly)
- *High Performance Spark* — Holden Karau & Rachel Warren (O'Reilly)

### Key APIs
- [`pyspark.sql.functions`](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/functions.html) — All built-in functions
- [`pyspark.sql.Window`](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.Window.html) — Window specifications
- [`pyspark.sql.types`](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/data_types.html) — Data types

---

## Tutorial Notebook

See [`pyspark-tutorial.ipynb`](./pyspark-tutorial.ipynb) for a hands-on, executable tutorial covering all topics with real examples and output.
