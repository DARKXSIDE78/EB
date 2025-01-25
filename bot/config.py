from bot.get_cfg import get_config
import re

def parse_auth_users(auth_users_string):
    auth_users = set()
    for user in auth_users_string.split(","):
        user = user.strip()
        if user.isdigit():  # Check if it's a numeric user ID
            auth_users.add(int(user))
        elif re.match(r"^@\w+$", user):  # Check if it's a valid username
            auth_users.add(user)
        else:
            print(f"Invalid user identifier: {user}")
    return auth_users

# Configuration


class Config(object):
    SESSION_NAME = get_config("SESSION_NAME", "@AniEncoderBot")
    APP_ID = int(get_config("APP_ID", "29478593"))
    API_HASH = get_config("API_HASH", "24c3a9ded4ac74bab73cbe6dafbc8b3e")
    LOG_CHANNEL = get_config("LOG_CHANNEL", "@teteetetsss")
    UPDATES_CHANNEL = get_config("UPDATES_CHANNEL", "@teteetetsss")
    AUTH_USERS = parse_auth_users(
    get_config("AUTH_USERS", "7086472788", should_prompt=True)
    )
    TG_BOT_TOKEN = get_config("TG_BOT_TOKEN", "7951337417:AAHCWTuLk0TfgOD-Vs4CUsuxBtMyDibcU4M")
    DOWNLOAD_LOCATION = get_config("DOWNLOAD_LOCATION", "downloads")
    BOT_USERNAME = get_config("BOT_USERNAME", "AniEncoderBot")
    MAX_FILE_SIZE = 2097152000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 2097152000
    DEF_THUMB_NAIL_VID_S = get_config("DEF_THUMB_NAIL_VID_S", "https://t.me/BatchBotLog/2251")
    HTTP_PROXY = get_config("HTTP_PROXY", None)
    MAX_MESSAGE_LENGTH = 4096
    FINISHED_PROGRESS_STR = get_config("FINISHED_PROGRESS_STR", "■")
    UN_FINISHED_PROGRESS_STR = get_config("UN_FINISHED_PROGRESS_STR", "▢")
    LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "Log.txt")
    SHOULD_USE_BUTTONS = get_config("SHOULD_USE_BUTTONS", False)
