"""
Logging setup module.
Configures structured logging for the application.
"""

import logging
import sys


def setup_logging(level: int = logging.INFO) -> logging.Logger:
    """
    Configure application logging to stdout with a standard format.

    Args:
        level: The logging level to set.

    Returns:
        The configured root logger.
    """
    logger = logging.getLogger("etl")
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(level)
    return logger
