import logging
from utils.config import dict

log_level = {'DEBUG': logging.DEBUG,
             'INFO': logging.INFO,
            }

file_handler = logging.FileHandler(filename='serve.log')
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
