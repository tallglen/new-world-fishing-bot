import logging
from utils.config import dict
from datetime import datetime

log_level = {'DEBUG': logging.DEBUG,
             'INFO': logging.INFO,
            }

file_handler = logging.FileHandler('{:%Y-%m-%d}.log'.format(datetime.now()))
stdout_handler = logging.StreamHandler()
handlers = [ file_handler, stdout_handler ]

logging.basicConfig(
    level=log_level.get(dict['log_lvl']),
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=handlers
)

def info(message):
    logging.info(message)

def debug(message):
    logging.debug(message)
