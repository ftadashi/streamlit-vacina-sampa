import logging

# Logging configuration
logging.basicConfig(format='[%(asctime)s]%(levelname)s:%(message)s', level=logging.DEBUG)

def log(t):
    debug(t)
    info(t)
    warn(t)
    error(t)
    critical(t)

def debug(t):
    #if logging.isEnabledFor(logging.DEBUG):
    logging.debug(t)

def info(t):
    #if logging.isEnabledFor(logging.INFO):
    logging.info(t)

def warn(t):
    #if logging.isEnabledFor(logging.WARNING):
    logging.warning(t)

def error(t):
    #if logging.isEnabledFor(logging.ERROR):
    logging.error(t)

def critical(t):
    #if logging.isEnabledFor(logging.CRITICAL):
    logging.critical(t)