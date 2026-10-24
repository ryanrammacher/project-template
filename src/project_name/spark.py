"""Create a Spark session that works on Databricks or locally."""
from pyspark.sql import SparkSession


def get_spark() -> SparkSession:
    """Use Databricks serverless if databricks-connect is installed, else local Spark."""
    try:
        from databricks.connect import DatabricksSession
    except ImportError:
        return SparkSession.builder.master("local[*]").appName("portfolio").getOrCreate()
    return DatabricksSession.builder.serverless().getOrCreate()
