import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = "logs"


if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILE = os.path.join(LOG_DIR, "app.log")


def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

   
    if logger.handlers:
        return logger

    
    formatter = logging.Formatter(
        "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
    )

   
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5 * 1024 * 1024,   # 5MB
        backupCount=3
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

   
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger