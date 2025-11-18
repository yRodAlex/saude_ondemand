from loguru import logger
import sys
from src.config.settings import settings
def configure_logger():
    logger.remove()
    level = settings.log.level.upper()
    logger.add(sys.stdout, level=level)
configure_logger()