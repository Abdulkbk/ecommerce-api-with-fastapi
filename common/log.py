import sys
import logging

__all__ = 'logger'

logger = logging.getLogger('readflow')
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler('logs/log.txt')

formatter = logging.Formatter(
  '%(levelname)s: %(asctime)s (file: %(filename)s, line: %(lineno)d, func: %(funcName)s) - %(message)s'
)

handler.setFormatter(formatter)
logger.addHandler(handler)
logger.addHandler(file_handler)