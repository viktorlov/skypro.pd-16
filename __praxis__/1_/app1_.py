import logging


def print_args(*args, **kwargs):
    logging.info(f'args: {args}')
    logging.info(f'kwargs: {kwargs}')
    result = [i for i in args]
    result.extend([{k: v} for k, v in kwargs.items()])
    return result


if __name__ == '__main__':
    # Configure the logger
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Call the function with some arguments
    z = print_args(*"name", a="surname", b=['first', 'second'])
    logging.info(f'Result: {z}')
