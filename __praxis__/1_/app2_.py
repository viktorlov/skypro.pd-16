import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def print_args(*args, **kwargs):
    logger.info(f'Received {len(args)} positional arguments and {len(kwargs)} keyword arguments')
    logger.debug(f'Positional arguments: {args}')
    logger.debug(f'Keyword arguments: {kwargs}')

    result = [i for i in args]
    result.extend([{k: v} for k, v in kwargs.items()])

    logger.info(f'Returning {len(result)} items')
    logger.debug(f'Result: {result}')

    return result


if __name__ == '__main__':
    z = print_args(*"name", a="surname", b=['first', 'second'])
    print(z)


"""
In the above code, we've imported the logging module and set up a basic configuration using the basicConfig function.
We've set the logging level to INFO, which means that log messages with a severity of INFO and above will be displayed.
We've also specified a format for the log messages.

We've then created a logger object using the __name__ attribute, which is the name of the current module. This allows
us to identify which module the log messages are coming from.

Inside the print_args function, we've added several logging statements. The logger.info statements log the number of
positional and keyword arguments received by the function and the number of items returned by the function. The
logger.debug statements log the actual arguments and result of the function, which can be useful for debugging purposes.

Finally, in the if __name__ == '__main__' block, we've called the print_args function with some sample arguments and
printed the result. When the program runs, the log messages will be displayed in the console.

You can customize the logging configuration to suit your needs, such as writing the log messages to a file or sending
them to a remote server.
"""