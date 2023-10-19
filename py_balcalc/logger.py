"""Default logger for the app"""

import logging

__all__ = ('logger',)

formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger = logging.getLogger('qui')
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)
