__all__ = ["logging"]

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logging.getLogger("telethon").setLevel(logging.WARNING)
