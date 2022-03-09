from config.constants import LOG_FILEPATH
from omdb_importer import OMDBImporter
from utils import (
    export_all_episodes_for_series_to_csv, 
    export_all_series_to_csv, 
    load_tracked_series_from_json,
    print_formatted_data
)

import logger.logger as logger
log = logger.setup_applevel_logger(log_filepath=LOG_FILEPATH)


if __name__ == "__main__":
    omdb_importer = OMDBImporter()

    # pull all series data and export CSV file
    all_series_data = omdb_importer.get_all_series_data()
    print_formatted_data(all_series_data)
    export_all_series_to_csv(all_series_data)

    # pull episode data for all series and export CSV files
    for series in load_tracked_series_from_json():
        title = series["title"]
        all_episodes_data = omdb_importer.get_all_episodes_data_of_series(series_title=title)
        log.info(f"all episodes data for series '{title}':")
        print_formatted_data(all_episodes_data)
        export_all_episodes_for_series_to_csv(all_episodes_data, title)
