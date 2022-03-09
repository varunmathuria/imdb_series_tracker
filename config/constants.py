from enum import Enum
import os


ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

ALL_SERIES_CSV_PATH = os.path.join(ROOT_DIR, "csv_files/all_series.csv")
LOG_FILEPATH = os.path.join(ROOT_DIR, "logs/stdout.log")
OMDB_API_TOKEN_FILEPATH = os.path.join(ROOT_DIR, "config/.secret/omdb_credentials.json")
OMDB_URL = "http://www.omdbapi.com"
SERIES_EPISODES_CSV_PATH = os.path.join(ROOT_DIR, "csv_files/all_episodes_{0}.csv")
TRACKED_SERIES_FILEPATH = os.path.join(ROOT_DIR, "config/tracked_series.json")
