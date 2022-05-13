from interfaces import ConnectorI
from pyspark import SparkConf
from pyspark.sql import SparkSession


class DbConnector(ConnectorI):
    def __init__(self, config):
        pass

    def _connect(self):
        pass

    def fetch(self, fetch_model):
        pass

