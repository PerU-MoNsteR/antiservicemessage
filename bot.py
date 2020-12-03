import os
import asyncio
from bot import bot
import logging
import random
import sys
from heroku3 import from_key

from telethon import TelegramClient, events, custom
from telethon.sessions import StringSession
from telethon.errors.rpcerrorlist import SessionPasswordNeededError, PhoneCodeInvalidError

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
APP_NAME = os.environ.get("APP_NAME", None)
API_KEY = os.environ.get("API_KEY", None)
HU_APP = from_key(API_KEY).apps()[APP_NAME]

bot = Client(":memory:",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)
