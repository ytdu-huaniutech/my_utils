import logging
import sys

basic_format = '%(asctime)s %(levelname)s:%(name)s: %(message)s'


def get_logger(name, level=logging.INFO, format=basic_format):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(logging.Formatter(format))
    logger.addHandler(handler)
    logger.propagate = False
    return logger


if __name__ == '__main__':
    logger = get_logger(__name__)
    logger.info('logger created')
