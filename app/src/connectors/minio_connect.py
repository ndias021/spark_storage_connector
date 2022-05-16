from interfaces import ConnectorI
from pyspark import SparkConf
from pyspark.sql import SparkSession
from models.models import MinioConnectModel, MinioFileModel


class MinioConnector(ConnectorI):
    def __init__(self, config):
        config = config
        self.spark = None
        self.spark_config = (SparkConf()
                             .set("spark.hadoop.fs.s3a.endpoint", config["endpoint"])
                             .set("spark.hadoop.fs.s3a.access.key", config["access_key"])
                             .set("spark.hadoop.fs.s3a.secret.key", config["secret_key"])
                             .set("spark.hadoop.fs.s3a.path.style.access", "true")
                             .set("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
                             .set("spark.hadoop.fs.s3a.connection.ssl.enabled", config["ssl_enabled"]))

    def _connect(self):
        self.spark = SparkSession.builder \
            .master("local") \
            .appName("Reading MinIO") \
            .config(conf=self.spark_config) \
            .getOrCreate()

    def fetch(self, fetch_model):
        self._connect()
        fetch_info = fetch_model
        bucket_name = fetch_info["bucket_name"]
        bucket_file_path = fetch_info["bucket_file_path"]
        df = self.spark.read.format("csv").\
            option("header", "true").\
            load(f"s3a://{bucket_name}/{bucket_file_path}")
        return df
