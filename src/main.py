from src.extract.extract_users_form import extract_users_form
from src.extract.extract_synthetic_workout import extract_synthetic_workout
from src.load.load_to_minio import upload_df_as_csv
def main():
    df1=extract_users_form()
    upload_df_as_csv(df1,"users_form","users_form_log_birthdate.csv")
    df2=extract_synthetic_workout()
    upload_df_as_csv(df2,"synthetic_workout","synthetic_realistic_workout.csv")
if __name__=='__main__': main()