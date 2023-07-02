from loguru import logger
import sys

logger.remove()
logger.add(
    sys.stderr,
    format="<blue>{time:HH:mm:ss!UTC}</blue> <yellow>[!!]</yellow> <green>{message}</green>",
    level="INFO",
    filter=lambda x: "INFO" in str(x["level"]),
)
logger.add(
    sys.stderr,
    format="<blue>{time:HH:mm:ss!UTC}</blue> <red>[!!]</red> <green>{message}</green>",
    level="DEBUG",
    filter=lambda x: "DEBUG" in str(x["level"]),
)
logger.add(
    sys.stderr,
    format="<blue>{time:HH:mm:ss!UTC}</blue> <white>[!!]</white> <green>{message}</green>",
    level="ERROR",
    filter=lambda x: "ERROR" in str(x["level"]),
)
