CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Instructions
 * Requirements
 * Improvements


INTRODUCTION
------------

Running `python3 main.py` pulls all series data for the series in tracked_series.json, 
and pulls all episode data for each series in tracked_series.json, 
and exports this data to CSV files.

Features:
- backfills imdbids into tracked_series.json, once series are retrieved
    - original tracked_series data in tracked_series_backup.json
- outputs data in tabular format, using the pandas library
- logs to file (logs/stdout.log) as well as console

INSTRUCTIONS
------------

 - Install the packages in requirements.txt
    - `pip3 install pandas`
 - Navigate to imdb_series_tracker/
 - Run `python3 main.py`


IMPROVEMENTS
------------

I would've liked to add the following improvements, but ran out of time.
In no particular order:

 - better and more detailed documentation that follows PEP8
 - clearer and better formatted code, also following PEP8
 - a CLI allowing the user to choose what they would like pulled and how
    - the CLI could include menu options and look nice
    - "--h" and "--v" options (help and verbose)
 - the user would be able to add new shows to track, and pull individual show data
    - these were listed as nice-to-haves for the future, but I would've liked to include the functionality anyway
    - when adding new shows, provide way for user to know if the pulled show is actually the show they wanted
        - perhaps print more info about retrieved show
        - similarly, if no show was retrieved
        - provide a way for user to input more details to get correct show, like year (use 'search' rather than 'get' on OMDB API)
 - options for console output of retrieved data
