import functools
import time
from typing import Callable, TypeVar, Any
from datetime import datetime

from src.utilities.loggers import get_logger
from src.config import config

logger = get_logger(__name__)


def retry(max_attempts= 3, delay= 1, backoff = 1):


    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            last_exception = None

            for attempt in range(1, max_attempts + 1):
                try:
                    logger.info(f"Executing {func.__name__} (attempt {attempt}/{max_attempts})")
                    result = func(*args, **kwargs)
                    logger.info(f"Γ£ô {func.__name__} succeeded on attempt {attempt}")
                    return result
                except Exception as e:
                    last_exception = e
                    logger.warning(f"{func.__name__} failed on attempt {attempt}: {str(e)}")

                    if attempt < max_attempts:
                        logger.info(f"Retrying in {current_delay}s...")
                        time.sleep(current_delay)
                        current_delay *= backoff
                    else:
                        logger.error(f"Γ£ù {func.__name__} failed after {max_attempts} attempts")

            raise last_exception

        return wrapper

    return decorator

