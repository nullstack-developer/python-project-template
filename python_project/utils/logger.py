import logging
import sys
from pathlib import Path
from types import TracebackType
from typing import Any, Optional

LOG_DIR_PATH = Path("./log")
LOG_DIR_PATH.mkdir(exist_ok=True, parents=True)
LOG_PATH = LOG_DIR_PATH / "log.log"
LOG_FORMATT = "[%(asctime)s] %(levelname)-8s >> %(name)s : %(lineno)4s - %(message)s"


class ConsoleFormatter(logging.Formatter):

    blue = "\x1b[34;20m"
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    formatter = LOG_FORMATT

    FORMATS = {
        logging.DEBUG: blue + formatter + reset,
        logging.INFO: grey + formatter + reset,
        logging.WARNING: yellow + formatter + reset,
        logging.ERROR: red + formatter + reset,
        logging.CRITICAL: bold_red + formatter + reset,
    }

    def format(self, record: logging.LogRecord) -> str:
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


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
    logger.propagate = False
    logger.setLevel(logging.DEBUG)

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console_formatter = ConsoleFormatter()
    console.setFormatter(console_formatter)
    logger.addHandler(console)

    file_handler = logging.FileHandler(filename=LOG_PATH)
    file_handler.setLevel(logging.INFO)
    file_formatter = logging.Formatter(LOG_FORMATT)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    return logger


def hook_exception(
    exc_type: Any,
    exc_value: BaseException,
    exc_traceback: Optional[TracebackType],
) -> None:
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)

    logger.exception(
        "Unexpected exception", exc_info=(exc_type, exc_value, exc_traceback)
    )


logger = make_logger("")
sys.excepthook = hook_exception
