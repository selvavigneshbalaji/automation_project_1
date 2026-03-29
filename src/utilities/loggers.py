import logging
import logging.handlers
from pathlib import Path
from typing import Optional
import colorlog
from src.config import config

class Logger:
    _instance = None
    _loggers = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def get_logger(name) :

        if name not in Logger._loggers:
            Logger._loggers[name] = Logger._configure_logger(name)
        return Logger._loggers[name]

    @staticmethod
    def _configure_logger(name) :

        logger = logging.getLogger(name)
        if logger.handlers:
            return logger
        log_config = config.logging_config
        log_level = log_config.get('level', 'INFO')
        log_format = log_config.get('format', '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        log_file = log_config.get('log_file', 'logs/automation.log')
        file_level = log_config.get('file_level', 'DEBUG')
        console_level = log_config.get('console_level', 'INFO')

        # Set logger level
        logger.setLevel(getattr(logging, log_level))

        # Create logs directory if it doesn't exist
        log_path = Path(log_file).parent
        log_path.mkdir(parents=True, exist_ok=True)

        # Console Handler with Color
        console_handler = logging.StreamHandler()
        console_handler.setLevel(getattr(logging, console_level))

        # Create color formatter
        color_formatter = colorlog.ColoredFormatter(
            '%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red,bg_white',
            }
        )
        console_handler.setFormatter(color_formatter)
        logger.addHandler(console_handler)

        # File Handler with Rotation
        file_handler = logging.handlers.RotatingFileHandler(
            log_file,
            maxBytes=10485760,  # 10MB
            backupCount=10
        )
        file_handler.setLevel(getattr(logging, file_level))

        file_formatter = logging.Formatter(log_format)
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

        return logger


def get_logger(name: str) -> logging.Logger:

    return Logger.get_logger(name)


if __name__ == "__main__":
    # Test logger
    test_logger = get_logger(__name__)
    test_logger.debug("This is a debug message")
    test_logger.info("This is an info message")
    test_logger.warning("This is a warning message")
    test_logger.error("This is an error message")
    test_logger.critical("This is a critical message")

