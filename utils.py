import json
import pandas as pd

from config.constants import (
    ALL_SERIES_CSV_PATH, 
    LOG_FILEPATH, 
    SERIES_EPISODES_CSV_PATH, 
    TRACKED_SERIES_FILEPATH
)

import logger.logger as logger
log = logger.setup_applevel_logger(log_filepath=LOG_FILEPATH)


def load_tracked_series_from_json():
    """Open tracked_series.json (file containing shows currently being tracked, 
    and return tracked series info, as a Python list of dictionaries."""
    with open(TRACKED_SERIES_FILEPATH, "r") as f:
        return json.load(f)

def backfill_tracked_series_imdbid(series_imdbid, series_title):
    """Backfill 'imdbid' of a series into tracked_series.json."""
    with open(TRACKED_SERIES_FILEPATH, "r+") as f:
        json_string = f.read()
        tracked_series = json.loads(json_string)
        tracked_series_copy = json.loads(json_string)
        count = 0
        index_series = -1
        for series in tracked_series:
            if series["title"] == series_title:
                index_series = count
            count += 1
        tracked_series_copy[index_series] = {"imdbid": series_imdbid, "title": series_title}
        f.seek(0)
        f.truncate(0)
        json.dump(tracked_series_copy, f)

def get_dataframe(data):
    """Return pandas DataFrame object from data as a Python object."""
    return pd.DataFrame(data)

def export_all_series_to_csv(all_series_data):
    """Export all series data to a CSV file, located at 'csv_files/all_series.csv'"""
    all_series_df = get_dataframe(all_series_data)
    all_series_df.to_csv(ALL_SERIES_CSV_PATH)

def export_all_episodes_for_series_to_csv(episodes_data, series_title):
    """Export all episodes data for a series to a CSV file, 
       located at 'csv_files/all_episodes_{series_title}.csv'"""
    episodes_df = get_dataframe(episodes_data)
    formatted_series_title = series_title.lower().replace(" ", "_")
    episodes_df.to_csv(SERIES_EPISODES_CSV_PATH.format(formatted_series_title))

def print_formatted_data(data):
    df = pd.DataFrame(data)
    print(df)
