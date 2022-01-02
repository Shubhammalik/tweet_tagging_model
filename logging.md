# LOGGING
Logging is used as a very powerful tool, in programming to get better understanding of the flow of a program.
Every program runs two loggers by default, i.e. root and main both with a default level of WARING.

[Reference Python Docs](https://docs.python.org/3/library/logging.html)

## Levels of logging (6)
Based on the severity and type of detail required, the logging level is defined for a project/module. Can be set by using **setLevel(level=logging.INFO)**

Functions associated for each level logging are **debug(), info(), warning(), error(), critical(), and exception()**
1) **NOTSET** (value=0) Initialize the logging level to nothing
2) **DEBUG** (value=10) Gives detailed information for diagnosis problem
3) **INFO** (value=20) Info is used for confirmation of things working fine
4) **WARNING** (value=30) - Warning indicate something unexpected or raise a concern
5) **ERROR** (value=40) - Error indicates a serious problem which can cause abnormal behaviours
6) **CRITICAL** (value=50) - A serious error indicating the program itself may not be able to run


## Basic Configurations
**basicConfig(\*\*args)** method is used to define root logger properties.

Your script/app needs to call this somewhere at least once, and once set then basicConfig() cannot be changed.
E.g. calling it from two different modules/files/functions to write logs to different files won't work for the second fucntion calling it.

Commonly used parameters for basicConfig() are **(arguments image below)**:
1) **level**: the root logger will be set to specified severity level
2) **filename**: specifies the name of file in which logs of root logger will be saved
3) **filemode**: can be used to specify the filemode for log file, append (default) **'a'** or write **'w'**, open in **+ mode (a+, w+)** if you want write and read operations   
4) **format** this is the format of the log message **(image below)**
5) **handlers** used to define handlers for root logger, all the level functions will call basicConfig() if root handlers are not defined

## Classes and functions
1) **Logger** this is the class whose function will be invoked on calling **getLogger()**
2) **getLogger()** will invoke object of class Logger, defaults to root, **getLogger(\_\_name__)** returns logger of main
3) **setLevel(level)** sets the logger level to the specified level
4) **getChild(name)** creates a calling logger child with the specified name
5) **addHandler(hldr)** adds the specified handler to the logger
6) **removeHandler(hldr)** removes the specified handler to the logger
7) **Formatter(\*\*args)** takes log formatting arguments to specify output format, added to handlers vai setFormatter(), point 10
8) **StreamHandler(stream)** Defines the output to console format, if stream is not set defaults to _sys.stderr_
9) **FileHandler(filename, mode='a')** sends logging output to disk file
10) **setFormatter(fmt)** used by handlers (added to loggers) to define the output format defined in **Formatter** (point 7)
11) **disable(level=CRITICAL)** Provides an override over logger's own level, disable all logging calls of level specified and below
12) **logging.propagate = True/False** If set to true (default) when invoking getLogger(), any event logged to this logger will be passed to handlers of ancestor loggers.

    If a handler is attached to a logger and its ancestor(s), the it may emit the same log multiple time. In general, its better to attach handler to the highest in hierarchy or root logger.

## Log configurations
1) **As Methods**: Logs can be defined in a python file using methods and class functions
2) **Config file**: Logs can be configured in a _.conf_ file and can be loaded via __fileConfig()__
3) **Dict file**: Logs can be defined as a dictionary in _yaml_ file and can be loaded via __dictConfig()__

### Log format attributes
![Log format arguments](/Users/shubham/PythonProjects/twitter_online_learning_sentiment/static/logs/log_format_arguments.jpg)
[Source](https://docs.python.org/3/library/logging.html#logrecord-attributes)

### basicConfig() keywords arguments
![BasicConfig](/Users/shubham/PythonProjects/twitter_online_learning_sentiment/static/logs/basic_config_arguments.jpg)
[Source](https://docs.python.org/3/library/logging.html#logging.basicConfig)