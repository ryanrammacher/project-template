"""Create a Spark session that works on Databricks or locally."""
from pyspark.sql import SparkSession


def get_spark() -> SparkSession:
    try:
        from databricks.connect import DatabricksSession
        return DatabricksSession.builder.serverless().getOrCreate()
    except Exception:
        return SparkSession.builder.master("local[*]").appName("portfolio").getOrCreate()