from pydantic import BaseModel
from typing import Optional, Dict


# MinIO
class MinioConnectModel(BaseModel):
    endpoint: str
    access_key: str
    secret_key: str
    ssl_enabled: Optional[bool]=False


class MinioFileModel(BaseModel):
    bucket_name: str
    bucket_file_path: str


class MinioModel(BaseModel):
    minio_config: MinioConnectModel
    remote_location: MinioFileModel

