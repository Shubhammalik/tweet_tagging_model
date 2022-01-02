import sys
import logging
from datetime import datetime


def create_logger():
    print('LOGGER 1')
    # Create new or get existing logger, gets main logger (different than root)
    logger = logging.getLogger(__name__)
    print(logger)
    # Set logger level to info but main is still DEBUG
    logger.setLevel(level=logging.INFO)

    # Creating File Handler to output logs to file
    # Use format as 'a' to append and 'w' to overwrite
    fileHandler = logging.FileHandler('logs/function_log_{:%Y-%m-%d}.log'.format(datetime.now()), 'a')
    fileHandler.setLevel(level=logging.WARNING)

    # Creating File Handler to output logs to console only
    consoleHandler = logging.StreamHandler(stream=sys.stdout)
    consoleHandler.setLevel(level=logging.INFO)

    # Defining formatter and adding it to handlers
    formatter = logging.Formatter(
        '[%(asctime)s] :: %(levelname)8s @ %(filename)s:%(lineno)s :: %(name)s :: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')

    fileHandler.setFormatter(formatter)
    consoleHandler.setFormatter(formatter)

    # Adding handlers to logger
    logger.addHandler(consoleHandler)
    logger.addHandler(fileHandler)
    # used if the code reinitialize the base logger (main/root) level
    # every message from child/new loggers is sent to main logger which reprints it to the console
    logger.propagate = False
    print(logger)
    logger.debug('A debug message')
    logger.info('An info message')
    logger.warning('Something is not right.')
    logger.error('A Major error has happened.')
    logger.critical('This is a critical logging message\n')
    return logger


def second_logger():
    print('LOGGER 2')
    handle = 'app_logger'
    formatter = logging.Formatter(
        '[%(asctime)s] :: %(levelname)8s @ %(filename)s:%(lineno)s :: %(name)s :: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')

    # Inheriting logging level from root logger (set to Debug)
    logger2 = logging.getLogger(handle)
    logger2.propagate = False
    print(logger2.handlers)
    new_consoleHandler = logging.StreamHandler(stream=sys.stdout)
    new_consoleHandler.setFormatter(formatter)
    new_consoleHandler.setLevel(level=logging.WARNING)
    logger2.addHandler(new_consoleHandler)
    print(logger2)
    logger2.setLevel(logging.ERROR)
    # Changing logging level to ERROR
    print(logger2)
    logger2.info('This will not print due to logger level Error')
    logger2.warning('Logger 2 warning')
    logger2.error('This is app logger\n')
    # Changing logging level to INFO but handler is still WARNING
    logger2.setLevel(logging.INFO)
    print(logger2)
    logger2.info('Logger level changed, still will not print due to handler level')
    logger2.warning('Logger 2 warning, this will print now')
    logger2.error('This is second error message')
    component_logger = logger2.getChild('child_app')
    component_logger.critical('this will get printed with the prefix app\n')
    return logger2


def main_logger():
    print('LOGGER 3')
    # getting main logger, unless changed main logger will inherit handlers of root
    logger3 = logging.getLogger(__name__)
    print(logger3)
    print(logger3.handlers)
    logger3.info('This will not print as handlers in main are cleared in logger 1\n')
    return logger3


def root_logger():
    print('LOGGER 4')
    # getting root logger
    logger4 = logging.getLogger()
    print(logger4)
    logger4.info('This is logger 4 running root logger\n')

    print('BASE LOGGER')
    name = 'root'
    logging.info(f'This is a {name} logger!\n')

    a = 5
    b = 0

    try:
        c = a / b
    except Exception as e:
        logger4.exception("Exception occurred")
    return logger4


# All inherited or new logger messages are propagated to root, to avoid printing on console set propagate to false
# [any logger].propagate = False

# This sets the root logger to write to stdout (your console)
# Your script/app needs to call this somewhere at least once
# By default the root logger is set to WARNING
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s :: %(levelname)s :: MODULE %(module)s'
                                                ' :: %(name)s :: Line No %(lineno)s :: %(message)s',
                    handlers=[logging.StreamHandler(stream=sys.stdout)])

logger1 = create_logger()

# To clear logger handlers as logger1 appends handlers to main, any other logger will also inherit them otherwise
while logger1.handlers:
    logger1.handlers.pop()

logger2 = second_logger()

logger3 = main_logger()

logger4 = root_logger()