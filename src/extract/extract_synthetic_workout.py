from pathlib import Path
from src.config.settings import settings
from src.utils.file_handler import read_csv
def extract_synthetic_workout():
    return read_csv(Path(settings.paths.data_input)/"synthetic_realistic_workout.csv")