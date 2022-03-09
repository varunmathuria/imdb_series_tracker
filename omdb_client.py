import json
import requests

from config.constants import LOG_FILEPATH, OMDB_API_TOKEN_FILEPATH, OMDB_URL

import logger.logger as logger
log = logger.setup_applevel_logger(log_filepath=LOG_FILEPATH)


class OMDBClient:
    """Sends GET requests to OMDB."""

    def __init__(self, api_key=None):
        if not api_key:
            api_key = self.load_omdb_credentials_json()
        self.api_key = api_key

    def load_omdb_credentials_json(self):
        """Gets apikey from secret credentials file."""
        with open(OMDB_API_TOKEN_FILEPATH, "r") as f:
            creds = json.load(f)
            return creds["OMDB_API_KEY"]
    
    def get_request(self, payload):
        """Sends GET request to OMDB."""
        return requests.get(OMDB_URL, params=payload).json()
