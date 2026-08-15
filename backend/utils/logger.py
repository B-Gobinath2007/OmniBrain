import logging
import sys
from backend.config import settings

def setup_logger():
    """Configures the standard Python logging for the application.
    
    Includes timestamp, log level, logger/module name, and message.
    Log level defaults to DEBUG if settings.DEBUG is True, else INFO.
    """
    log_level = logging.DEBUG if settings.DEBUG else logging.INFO

    # Clear existing handlers to avoid duplication
    root = logging.getLogger()
    if root.handlers:
        for handler in root.handlers:
            root.removeHandler(handler)

    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(levelname)s - [%(name)s] - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

    logger = logging.getLogger("OmniBrain")
    return logger

logger = setup_logger()
