from dataclasses import dataclass
import os
from pathlib import Path
from dotenv import load_dotenv
BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env", override=False)
@dataclass
class MinioSettings:
    endpoint: str
    access_key: str
    secret_key: str
    secure: bool
    raw_bucket: str
@dataclass
class HevySettings:
    base_url: str
    timeout: int
@dataclass
class PathSettings:
    data_input: Path
    data_output: Path
@dataclass
class LogSettings:
    level: str
    json_format: bool
@dataclass
class Settings:
    minio: MinioSettings
    hevy: HevySettings
    paths: PathSettings
    log: LogSettings
def get_settings() -> Settings:
    data_input = Path(os.getenv("DATA_INPUT_PATH","/app/data/input"))
    data_output = Path(os.getenv("DATA_OUTPUT_PATH","/app/data/output"))
    return Settings(
      minio=MinioSettings(
        endpoint=os.getenv("MINIO_ENDPOINT","minio:9000"),
        access_key=os.getenv("MINIO_ACCESS_KEY","minioadmin"),
        secret_key=os.getenv("MINIO_SECRET_KEY","minioadmin"),
        secure=os.getenv("MINIO_SECURE","false")=="true",
        raw_bucket=os.getenv("MINIO_RAW_BUCKET","raw")
      ),
      hevy=HevySettings(
        base_url=os.getenv("HEVY_API_BASE_URL"),
        timeout=int(os.getenv("HEVY_API_TIMEOUT","10"))
      ),
      paths=PathSettings(
        data_input=data_input,
        data_output=data_output
      ),
      log=LogSettings(
        level=os.getenv("LOG_LEVEL","INFO"),
        json_format=os.getenv("LOG_FORMAT_JSON","false")=="true"
      )
    )
settings=get_settings()