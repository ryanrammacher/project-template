"""Load raw data."""
from pathlib import Path

from pyspark.sql import DataFrame, SparkSession

RAW_DIR = Path("data/raw")


def load_raw(spark: SparkSession, filename: str) -> DataFrame:
    """Read a CSV from data/raw/ into a Spark DataFrame."""
    return spark.read.csv(str(RAW_DIR / filename), header=True, inferSchema=True)