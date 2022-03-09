from config.constants import LOG_FILEPATH
import logging
import sys

APP_LOGGER_NAME = "omdb_importer_logger"


def setup_applevel_logger(logger_name="omdb_importer", log_filepath=LOG_FILEPATH):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="%(asctime)s %(levelname)-6s [%(filename)s:%(lineno)d] %(message)s",
        datefmt="%Y-%m-%d:%H:%M:%S"
    )

    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(formatter)
    logger.handlers.clear()
    logger.addHandler(sh)

    if log_filepath:
        fh = logging.FileHandler(log_filepath, mode='w')
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger


def get_logger(module_name):
    return logging.getLogger(APP_LOGGER_NAME).getChild(module_name)
