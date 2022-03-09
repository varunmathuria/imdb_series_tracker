from config.constants import LOG_FILEPATH
from omdb_client import OMDBClient
from utils import backfill_tracked_series_imdbid, load_tracked_series_from_json

import logger.logger as logger
log = logger.setup_applevel_logger(log_filepath=LOG_FILEPATH)


class OMDBImporter:
    """Uses OMDBClient to request data from OMDB."""

    def __init__(self):
        self.omdb_client = OMDBClient()
        self.tracked_series = load_tracked_series_from_json()
        self.default_params = {
            "plot": "full",
        }

    def get_omdb(self, params, short_plot=False):
        """Adds default_params and apikey to params, calls omdb_client.get_request."""
        payload = params | self.default_params
        payload = params | {"apikey": self.omdb_client.api_key}
        if short_plot:
            payload |= {"plot": "short"}
        return self.omdb_client.get_request(payload)

    def get_series(self, series_imdbid=None, series_title=None):
        """Gets a series' data from OMDB."""
        params = {
            "i": series_imdbid,
            "t": series_title,
            "type": "series",
        }
        series_data = self.get_omdb(params)
        return series_data

    def get_season(self, season_num, series_imdbid=None, series_title=None):
        """Gets a series' season's data from OMDB."""
        params = {
            "i": series_imdbid, 
            "t": series_title,
            "Season": season_num, 
            "type": "series",
        }
        season_data = self.get_omdb(params)
        backfill_tracked_series_imdbid(season_data["imdbID"], season_data["Title"])
        return season_data

    def get_episode(self, season_num, episode_num, series_imdbid=None, series_title=None):
        """Gets a specific episode's data from OMDB."""
        params = {
            "i": series_imdbid,
            "t": series_title,
            "Season": season_num,
            "Episode": episode_num,
            "type": "episode",
        }
        return self.get_omdb(params)
    
    def get_all_series_data(self):
        """Gets series level data for all series being tracked in tracked_series.json."""
        self.tracked_series = load_tracked_series_from_json()
        all_series_data = []
        num_series_retrieved = 0
        log.info(f"retrieving data for all series being tracked")
        for series in self.tracked_series:
            imdbid = series["imdbid"]
            title = series["title"]
            if imdbid:
                series_data = self.get_series(series_imdbid=imdbid)
            else:
                series_data = self.get_series(series_title=title)
            all_series_data.append(series_data)
            num_series_retrieved += 1
            log.info(f"retrieved series data for '{title}'")
            log.info(f"retrieved data for {num_series_retrieved} series")
            if not imdbid:
                imdbid = series_data["imdbID"]
                backfill_tracked_series_imdbid(imdbid, title)
                log.info(f"backfilled imdbid {imdbid} for series '{title}' into tracked_series.json")
        return all_series_data
    
    def get_all_episodes_data_of_series(self, series_imdbid=None, series_title=None):
        """Gets all episode data of a series."""
        all_episodes_data = []
        if series_imdbid:
            series_data = self.get_series(series_imdbid=series_imdbid)
        else:
            series_data = self.get_series(series_title=series_title)
        num_seasons = int(series_data["totalSeasons"])
        title = series_data["Title"]
        imdbid = series_data["imdbID"]
        log.info(f"retrieving all episode data for '{title}', {num_seasons} season(s)")
        for season_num in range(1, num_seasons+1):
            episode_num = 1
            while True:
                episode_data = self.get_episode(series_imdbid=imdbid, series_title=title, season_num=season_num, episode_num=episode_num)
                if episode_data["Response"] == "False":
                    break
                all_episodes_data.append(episode_data)
                log.info(f"retrieved episode data for season {season_num} episode {episode_num}")
                episode_num += 1
        return all_episodes_data
