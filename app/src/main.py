import logging
from connectors.minio_connect import MinioConnector
from connectors.db_connect import DbConnector

# READING THE DATA FROM MINIO
CONFIG_MINIO = {
    "endpoint": "http://localhost:9000",
    "access_key": "minioadmin",
    "secret_key": "minioadmin",
    "ssl_enabled": False
}
mc = MinioConnector(config=CONFIG_MINIO)

fetch_info = {
    "bucket_name": "dias-personal",
    "bucket_file_path": "test.csv"
}
df = mc.fetch(fetch_model=fetch_info)
print(df.show(2))

logging.info("Done MinIO")

# READING THE DATA FROM POSTGRES
CONFIG_POSTGRES = {
    "db_host": "localhost",
    "db_port": "5432",
    "db_name": "world-db",
    "db_user": "world",
    "db_pass": "world123"
}
db_c = DbConnector(config=CONFIG_POSTGRES)

fetch_info = {
    "table": "city"
}
df = db_c.fetch(fetch_model=fetch_info)
print(df.show(2))
logging.info("Done Postgres")