from datetime import date
from io import BytesIO
from src.utils.minio_client import get_minio_client
def upload_df_as_csv(df, dataset, filename):
    client=get_minio_client()
    object_name=f"{dataset}/ingestion_date={date.today()}/{filename}"
    buff=BytesIO()
    df.to_csv(buff,index=False)
    buff.seek(0)
    client.put_object("raw",object_name,buff,len(buff.getvalue()))