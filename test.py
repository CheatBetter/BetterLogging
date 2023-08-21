from betterlogs import logger
from colorama import Fore, Style

logger = logger.Logger(name="BetterLogs", base_color=Fore.BLUE, base_style=Style.DIM,
                       time=True, time_color=Fore.BLUE, time_style=Style.BRIGHT)

logger.log("test")
logger.debug("test")
logger.warning("test")
logger.error("test")
logger.critical("test")