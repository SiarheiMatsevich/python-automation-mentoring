import importlib.util
import sys
from importlib.metadata import version
import logging
import argparse

logger = logging.getLogger()


def get_package_path(package_name: str) -> str:
    """
    Returns a path to given package if it exists. Otherwise, returns 'Package not found'
    """
    package = importlib.util.find_spec(package_name)
    if not package:
        logger.error('Package not found')
        return 'Package not found'
    else:
        logger.warning(package.__doc__)
        logger.info(package.origin)
        logger.debug(version(package_name))
        return package.origin


def parse_cmd_args():

    logging_levels = list(logging.getLevelNamesMapping().keys())
    package_name_help = 'Package name to get path for'
    file_log_level_help = ('Level of log records being written to \'package_path.log\' file.'
                           f'Possible values: {logging_levels}')
    console_log_level_help = ('Level of log records being printed to stderr stream'
                              f'Possible values: {logging_levels}')

    parser = argparse.ArgumentParser(description=get_package_path.__doc__)
    parser.add_argument('package name', help=package_name_help)
    parser.add_argument('--file_log_level', default=None, help=file_log_level_help)
    parser.add_argument('--console_log_level', default=None, help=console_log_level_help)

    args, _ = parser.parse_known_args()
    file_level = args.file_log_level
    console_level = args.console_log_level

    if file_level and file_level in logging_levels:
        logger.setLevel(logging.NOTSET)
        file_handler = logging.FileHandler('package_path.log')
        file_handler.setLevel(file_level)
        logger.addHandler(file_handler)
    elif file_level and file_level not in logging_levels:
        raise AttributeError('Incorrect logging level for \'--file_log_level\'. '
                             'Please use --help to see possible levels')

    if console_level and console_level in logging_levels:
        logger.setLevel(logging.NOTSET)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(console_level)
        logger.addHandler(console_handler)
    elif console_level and console_level not in logging_levels:
        raise AttributeError('Incorrect logging level for \'--console_log_level\'. '
                             'Please use --help to see possible levels')
    return args.path


if __name__ == '__main__':
    package_name = parse_cmd_args()
    get_package_path(package_name)
