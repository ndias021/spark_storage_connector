import logging
from connectors.minio_connect import MinioConnector
from connectors.db_connect import DbConnector

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

logging.info("Done")


CONFIG_POSTGRES = {

}
db_c = DbConnector(config=CONFIG_POSTGRES)
fetch_info = {
    "table": "city"
}
df = db_c.fetch(fetch_model=fetch_info)

print(df.show(2))
