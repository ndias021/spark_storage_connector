from helpers.minio_connect import MinioConnector

config = {
    "endpoint": "http://localhost:9000",
    "access_key": "minioadmin",
    "secret_key": "minioadmin",
    "ssl_enabled": False
}

mc = MinioConnector(config=config)
fetch_info = {
    "bucket_name": "dias-personal",
    "bucket_file_path": "test.csv"
}
df = mc.fetch(fetch_model=fetch_info)
print(df.show(2))

print("Done")
