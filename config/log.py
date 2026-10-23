from loguru import logger
from pathlib import Path
import sys

logger.remove()  # remove default logger

log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(exist_ok=True)

logger.add(sys.stderr, level="INFO", colorize=True)  # log in console

logger.add(  # log in file
    log_dir / "tg_bt.log",
    format="{time} {level} {message}",
    level="INFO",
    rotation="1 MB",
    retention="10 days",
)
