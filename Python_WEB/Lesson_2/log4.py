import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(level=logging.INFO)
handler = RotatingFileHandler(
    "rotating_log", maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf-8"
)

logger = logging.getLogger()
logger.addHandler(handler)

logger.info("a")
logger.error("b")
