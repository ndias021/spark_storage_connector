from interfaces import ConnectorI
from pyspark import SparkConf
from pyspark.sql import SparkSession


class DbConnector(ConnectorI):
    def __init__(self, config):
        config = config
        self.spark = None
        self.spark_config = (SparkConf()
                             .set("spark.jars", "postgresql-42.2.14.jar"))

    def _connect(self):
        self.spark = SparkSession.builder \
            .master("local") \
            .appName("Reading Postgres") \
            .config(conf=self.spark_config) \
            .getOrCreate()

    def fetch(self, fetch_model):
        self._connect()
        fetch_info = fetch_model
        jdbcDF = self.spark.read.format("jdbc"). \
            options(
            url='jdbc:postgresql://localhost:5432/world-db',
            dbtable='city',
            user='world',
            password='world123',
            driver='org.postgresql.Driver'). \
            load()
        print(jdbcDF.printSchema())
        return jdbcDF
