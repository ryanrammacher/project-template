"""Analysis, aggregations, and charts."""
import pyspark.sql.functions as F
from pyspark.sql import DataFrame


def count_by(df: DataFrame, col: str) -> DataFrame:
    """Row counts per category, largest first."""
    return df.groupBy(col).count().orderBy(F.desc("count"))