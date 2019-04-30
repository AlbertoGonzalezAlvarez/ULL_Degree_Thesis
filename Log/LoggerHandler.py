import logging
import time
import inspect

logger = logging.getLogger(__name__)

class LoggerHandler:

    @staticmethod
    def log(msg):
        _stack = inspect.stack()[1]
        className = _stack[0].f_locals['self'].__class__.__name__.upper()
        print(f"> {time.strftime('%H:%M:%S')} [{className}][INFO] -> {msg}")

    @staticmethod
    def error(msg):
        _stack = inspect.stack()[1]
        className = _stack[0].f_locals['self'].__class__.__name__.upper()
        logger.error(f"> {time.strftime('%H:%M:%S')} [{className}][ERROR] -> {msg}")

    @staticmethod
    def warning(msg):
        _stack = inspect.stack()[1]
        className = _stack[0].f_locals['self'].__class__.__name__.upper()
        logger.warning(f"> {time.strftime('%H:%M:%S')} [{className}][WARNING] -> {msg}")