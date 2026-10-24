"""Clean and reshape data."""
import re
from pyspark.sql import DataFrame


def snake_case(name: str) -> str:
    """'Trip Distance (mi)' -> 'trip_distance_mi'."""
    return re.sub(r"[^0-9a-z]+", "_", name.strip().lower()).strip("_")


def clean_columns(df: DataFrame) -> DataFrame:
    """Rename all columns to snake_case."""
    return df.toDF(*[snake_case(c) for c in df.columns])