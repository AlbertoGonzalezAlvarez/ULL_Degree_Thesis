import logging
import time
import sys

logger = logging.getLogger(__name__)

class LoggerHandler:

    @staticmethod
    def log(className: str = "", msg: str = "") -> None:
        print(f"> {time.strftime('%H:%M:%S')} [{className}][INFO] -> {msg}")
        sys.stdout.flush()

    @staticmethod
    def error(className: str = "", msg: str = "") -> None:
        logger.error(f"> {time.strftime('%H:%M:%S')} [{className}][ERROR] -> {msg}")
        logger.error(f"> {time.strftime('%H:%M:%S')} [{className}][ERROR] -> Exiting program")
        sys.exit()

    @staticmethod
    def warning(className: str = "", msg: str = "") -> None:
        logger.warning(f"> {time.strftime('%H:%M:%S')} [{className}][WARNING] -> {msg}")