
import logging

def print_info_log(msg, log_level):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    logger.log(log_level, msg)


"""
In this example, the function initializes a logger with the name of the current module (__name__) and sets the logger level to DEBUG. It also sets up a StreamHandler that logs to the console, with a log level specified by the log_level parameter. The log message is formatted using a Formatter object, and the handler is configured to use this formatter.

The logger.log() method is then used to log the message with the specified log level.

With this implementation, you can use the logging module's built-in functionality to customize the log levels, log format, and output destination. You can also configure additional handlers to log to files, databases, or other destinations, and set up a hierarchy of loggers to organize your logs.
"""

