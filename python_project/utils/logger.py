import logging
import sys
from pathlib import Path
from types import TracebackType
from typing import Optional

LOG_DIR_PATH = Path("./log")
LOG_DIR_PATH.mkdir(exist_ok=True, parents=True)
LOG_PATH = LOG_DIR_PATH / "log.log"


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
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)-8s >> %(name)s : %(lineno)4s - %(message)s"
    )

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)
    logger.addHandler(console)

    file_handler = logging.FileHandler(filename=LOG_PATH)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    def hook_exception(
        exc_type,
        exc_value: BaseException,
        exc_traceback: Optional[TracebackType],
    ) -> None:
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)

        logger.exception(
            "Unexpected exception", exc_info=(exc_type, exc_value, exc_traceback)
        )

    sys.excepthook = hook_exception
    return logger
