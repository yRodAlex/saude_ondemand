from pathlib import Path
from src.config.settings import settings
from src.utils.file_handler import read_csv
def extract_users_form():
    return read_csv(Path(settings.paths.data_input)/"users_form_log_birthdate.csv")