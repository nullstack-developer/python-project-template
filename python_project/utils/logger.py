import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path
from types import TracebackType
from typing import Optional

DEBUG_LOG_PATH = Path("./log/debug.log")
DEBUG_LOG_MAX_SIZE = 10 * 1024 * 1024
DEBUG_LOG_COUNT = 10
ERROR_LOG_PATH = Path("./log/error.log")


def make_logger(name: Optional[str]) -> logging.Logger:
    """Make logging instance.
    Only using `% formatting`, not f-string, format string.
    Format: [YYYY-MM-DD hh:mm:ss,ms] <LEVEL>  >> <FILENAME> : <LINENO> - <MESSAGE>


    Args:
        name Optional(str): Set `__name__` when calling logger.

    Returns:
        logging.Logger: Logging instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)-8s >> %(name)s : %(lineno)4s - %(message)s"
    )

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)
    logger.addHandler(console)

    debug_file_handler = RotatingFileHandler(
        DEBUG_LOG_PATH,
        maxBytes=DEBUG_LOG_MAX_SIZE,
        backupCount=DEBUG_LOG_COUNT,
    )
    debug_file_handler.setLevel(logging.DEBUG)
    debug_file_handler.setFormatter(formatter)
    logger.addHandler(debug_file_handler)

    error_file_handler = logging.FileHandler(filename=ERROR_LOG_PATH)
    error_file_handler.setLevel(logging.DEBUG)
    error_file_handler.setFormatter(formatter)
    logger.addHandler(error_file_handler)
    return logger


def hook_exception(
    exc_type,
    exc_value: BaseException,
    exc_traceback: Optional[TracebackType],
) -> None:
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)

    logger.error("Unexpected exception", exc_info=(exc_type, exc_value, exc_traceback))


if __name__ == "__main__":
    logger = make_logger(__name__)
    sys.excepthook = hook_exception
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")
    raise RuntimeError("Test unhandled")
