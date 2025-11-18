from minio import Minio
from src.config.settings import settings
def get_minio_client():
    return Minio(settings.minio.endpoint,
                 access_key=settings.minio.access_key,
                 secret_key=settings.minio.secret_key,
                 secure=settings.minio.secure)