"""Analysis, aggregations, and charts."""
from pyspark.sql import DataFrame
import pyspark.sql.functions as F


def count_by(df: DataFrame, col: str) -> DataFrame:
    """Row counts per category, largest first."""
    return df.groupBy(col).count().orderBy(F.desc("count"))