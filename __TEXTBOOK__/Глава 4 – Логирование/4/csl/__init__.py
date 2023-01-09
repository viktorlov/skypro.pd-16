import logging


def create_and_set_loggers():

    # logger

    logger = logging.getLogger("logger")
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

    # new_post_logger

    new_post_logger = logging.getLogger("new_post_logger")
    new_post_logger.setLevel(logging.DEBUG)

    console_POST_handler = logging.StreamHandler()
    console_POST_handler.setLevel(logging.DEBUG)
    new_post_logger.addHandler(console_POST_handler)

    file_POST_handler = logging.FileHandler('POST.log')
    file_POST_handler.setLevel(logging.DEBUG)
    new_post_logger.addHandler(file_POST_handler)

    # delete_logger

    delete_logger = logging.getLogger("delete_logger")
    delete_logger.setLevel(logging.DEBUG)

    console_DELETE_handler = logging.StreamHandler()
    console_DELETE_handler.setLevel(logging.DEBUG)
    delete_logger.addHandler(console_DELETE_handler)

    file_DELETE_handler = logging.FileHandler('DELETE.log')
    file_DELETE_handler.setLevel(logging.DEBUG)
    delete_logger.addHandler(file_DELETE_handler)

    # logger_404

    logger_404 = logging.getLogger("logger_404")
    logger_404.setLevel(logging.DEBUG)

    file_404_handler = logging.FileHandler('404.log')
    file_404_handler.setLevel(logging.DEBUG)
    logger_404.addHandler(file_404_handler)

