import yaml
import logging
import logging.config


def create_logger():
    handle = 'fileLogger'
    print(f'LOGGER 1 - {handle}')
    logger = logging.getLogger(handle)
    print(logger)
    print(logger.handlers)
    logger.debug('A debug message')
    logger.info('An info message')
    logger.warning('Something is not right.')
    logger.error('A Major error has happened.')
    logger.critical('This is a critical logging message\n')
    return logger


def second_logger():
    handle = 'streamLogger'
    print(f'LOGGER 2 - {handle}')
    logger2 = logging.getLogger(handle)
    print(logger2)
    print(logger2.handlers)
    logger2.debug('This will not print due to logger level Error')
    logger2.info('This is info, will not print due to handler level WARNING')
    logger2.warning('Logger 2 warning')
    logger2.error('This is logger error\n')
    # Changing logging level to INFO but handler is still WARNING
    logger2.setLevel(logging.DEBUG)
    print(logger2)
    logger2.debug('Logger level changed, still will not print due to handler level')
    logger2.warning('This is second warning message')
    logger2.error('This is second error message\n')
    component_logger = logger2.getChild('child_app')
    component_logger.info('this will not be printed as child inherits parents handlers')
    component_logger.warning('this warning gets printed with the prefix app\n')
    component_logger.setLevel(logging.INFO)
    component_logger.info('still won\'t be printed as child inherits parents handlers')
    component_logger.setLevel(logging.ERROR)
    component_logger.warning('this warning wont be printed now')
    component_logger.critical('this critical get printed with the prefix app\n')
    return logger2


def main_logger():
    print('LOGGER 3 - main')
    # getting main logger, unless changed main logger will use/invoke handlers of root
    logger3 = logging.getLogger(__name__)
    print(logger3)
    print(logger3.handlers)
    logger3.debug('This will not print, level of root handler is warning\n')
    logger3.info('This will not print, level of root handler is warning\n')
    logger3.warning('This will print warning level of main\n')
    return logger3


def root_logger():
    print('LOGGER 4 - root')
    # getting root logger
    logger4 = logging.getLogger()
    print(logger4)
    print(logger4.handlers)
    logger4.warning('This is logger 4 running root logger')

    print('BASE LOGGER')
    name = 'root'
    logging.critical(f'This is a {name} logger!\n')

    a = 5
    b = 0

    try:
        c = a / b
    except Exception as e:
        logger4.exception("Exception occurred")
    return logger4


## Takes the argument config/yaml
type = 'config'

if type == 'config':
    print('Logging form config file')
    logging.config.fileConfig(fname='config/log_config.conf', disable_existing_loggers=False)
elif type == 'yaml':
    print('Logging form YAML file')
    with open('config/log_yaml.yaml', 'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
else:
    print('Unsupported type format')

logger1 = create_logger()

logger2 = second_logger()

logger3 = main_logger()

logger4 = root_logger()
