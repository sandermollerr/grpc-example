import logging
import sys
from logging.config import dictConfig

DEFAULT_HANDLER = "json"

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "plain": {
            "format": "%(asctime)s %(levelname)s %(name)s %(lineno)d : %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "json": {
            "class": "ns.logging.formatters.tracing.TraceJsonFormatter",
            "format": "%(asctime)s %(created)f %(filename)s %(funcName)s %(levelname)s %(levelno)s %(lineno)d "
            "%(message)s %(module)s %(msecs)d %(name)s %(pathname)s %(process)d %(processName)s "
            "%(thread)d %(threadName)s %(traceID)s %(spanID)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "plain": {
            "level": "DEBUG",
            "formatter": "plain",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",  # Default is stderr
        },
        "json": {
            "level": "DEBUG",
            "formatter": "json",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",  # Default is stderr
        },
    },
    "loggers": {
        "": {
            "handlers": [DEFAULT_HANDLER],
            "level": "INFO",
            "propagate": False,
        },  # root logger
        "src": {"handlers": [DEFAULT_HANDLER], "level": "DEBUG", "propagate": False},
        "libraries": {
            "handlers": [DEFAULT_HANDLER],
            "level": "DEBUG",
            "propagate": False,
        },
        "gunicorn": {
            "handlers": [DEFAULT_HANDLER],
            "level": "INFO",
            "propagate": False,
        },
        "gunicorn.access": {
            "handlers": [DEFAULT_HANDLER],
            "level": "INFO",
            "propagate": False,
        },
        "gunicorn.error": {
            "handlers": [DEFAULT_HANDLER],
            "level": "INFO",
            "propagate": False,
        },
        "unicorn": {"handlers": [DEFAULT_HANDLER], "level": "INFO", "propagate": False},
        "uvicorn.access": {
            "handlers": [DEFAULT_HANDLER],
            "level": "INFO",
            "propagate": False,
        },
        "uvicorn.error": {
            "handlers": [DEFAULT_HANDLER],
            "level": "INFO",
            "propagate": False,
        },
        "grpc": {
            "handlers": [DEFAULT_HANDLER],
            "level": "INFO",
            "propagate": False,
        },
    },
    "root": {
        "level": "INFO",
        "handlers": [DEFAULT_HANDLER],
        "propagate": True,
    },
}


def apply_logging_config() -> None:
    """
    Apply logging configuration
    :return:
    """
    dictConfig(LOGGING_CONFIG)


logger = logging.getLogger(__name__)


def setup_exception_logging_hook() -> None:
    """
    Setup logging hook for unhandled exceptions
    :return:
    """

    def log_exception(exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return

        logger.critical(
            "Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback)
        )

    sys.excepthook = log_exception
