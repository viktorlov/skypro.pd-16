import logging


def create_and_set_loggers():

    logger = logging.getLogger("debug")
    logger.setLevel(logging.DEBUG)

    console_DEBUG_handler = logging.StreamHandler()
    console_DEBUG_handler.setLevel(logging.DEBUG)
    logger.addHandler(console_DEBUG_handler)

    file_DEBUG_handler = logging.FileHandler('DEBUG.log')
    file_DEBUG_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_DEBUG_handler)

    file_ERROR_handler = logging.FileHandler('ERROR.log')
    file_ERROR_handler.setLevel(logging.ERROR)
    logger.addHandler(file_ERROR_handler)
