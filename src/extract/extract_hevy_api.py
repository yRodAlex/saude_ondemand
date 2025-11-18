import requests, pandas as pd
from src.config.settings import settings
def fetch_hevy_user_data(user_id, api_key):
    url=f"{settings.hevy.base_url}/v1/workouts"
    r=requests.get(url,headers={"Authorization":f"Bearer {api_key}"},timeout=settings.hevy.timeout)
    r.raise_for_status()
    data=r.json()
    if isinstance(data,dict) and "workouts" in data: data=data["workouts"]
    df=pd.DataFrame(data)
    df["user_id"]=user_id
    return df