from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "Hɪ..., I ᴀᴍ **Sᴀsᴜᴋᴇ Uᴄʜɪʜᴀ**!\n\nI ᴄᴀɴ ᴇɴᴄᴏᴅᴇ ᴠɪᴅᴇᴏ ɪɴ ᴀɴʏ ᴄᴏᴅᴇᴄ (ᴇ.ɢ. ʟɪʙx264, ʟɪʙx265) ᴡɪᴛʜ ᴛʜᴇ ғᴀsᴛᴇʀ sᴇᴛᴛɪɴɢs ᴀʟʀᴇᴀᴅʏ ʙᴜɪʟᴛɪɴ.\n\nYᴏᴜ ᴄᴀɴ ᴇᴀsɪʟʏ ᴄʜᴀɴɢᴇ ᴍʏ sᴇᴛᴛɪɴɢs ᴛʜʀᴏᴜɢʜ ᴄᴏᴍᴍᴀɴᴅs."
   
    ABS_TEXT = "Pʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ʙᴇ sᴇʟғɪsʜ."
    
    FORMAT_SELECTION = "Sᴇʟᴇᴄᴛ ᴛʜᴇ ᴅᴇsɪʀᴇᴅ ғᴏʀᴍᴀᴛ: <a href='{}'>ғɪʟᴇ sɪᴢᴇ ᴍɪɢʜᴛ ʙᴇ ᴀᴘᴘʀᴏxɪᴍᴀᴛᴇ</a> \nIғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴇᴛ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ, sᴇɴᴅ ᴘʜᴏᴛᴏ ʙᴇғᴏʀᴇ ᴏʀ ǫᴜɪᴄᴋʟʏ ᴀғᴛᴇʀ ᴛᴀᴘᴘɪɴɢ ᴏɴ ᴀɴʏ ᴏғ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs.\nYᴏᴜ ᴄᴀɴ ᴜsᴇ /ᴅᴇʟᴇᴛᴇᴛʜᴜᴍʙɴᴀɪʟ ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴀᴜᴛᴏ-ɢᴇɴᴇʀᴀᴛᴇᴅ ᴛʜᴜᴍʙɴᴀɪʟ."
    
    
    DOWNLOAD_START = "⚡ Dᴏᴡɴʟᴏᴀᴅɪɴɢ...\n"
    
    UPLOAD_START = "⚡ Uᴘʟᴏᴀᴅɪɴɢ...\n"
    
    COMPRESS_START = "⚡ Eɴᴄᴏᴅɪɴɢ..."
    
    RCHD_BOT_API_LIMIT = "sɪᴢᴇ ɢʀᴇᴀᴛᴇʀ ᴛʜᴀɴ ᴍᴀxɪᴍᴜᴍ ᴀʟʟᴏᴡᴇᴅ sɪᴢᴇ (50MB). Nᴇᴠᴇʀᴛʜʟᴇss, ᴛʀʏɪɴɢ ᴛᴏ ᴜᴘʟᴏᴀᴅ."
    
    RCHD_TG_API_LIMIT = "Fɪʟᴇ ɢʀᴇᴀᴛᴇʀ ᴛʜᴀɴ 1.95GB ᴄᴀɴ ɴᴏᴛ ʙᴇ ᴇɴᴄᴏᴅᴇᴅ ᴅᴜᴇ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ʟɪᴍɪᴛᴀᴛɪᴏɴs"
    
    COMPRESS_SUCCESS = "Eɴᴄᴏᴅᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ..."

    COMPRESS_PROGRESS = "⏳ ETA: {} 👁️‍🗨️ Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Cᴜsᴛᴏᴍ ᴠɪᴅᴇᴏ / ғɪʟᴇ ᴛʜᴜᴍʙɴᴀɪʟ sᴀᴠᴇᴅ. Tʜɪs ɪᴍᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴜsᴇᴅ ɪɴ ᴛʜᴇ ᴠɪᴅᴇᴏ / ғɪʟᴇ."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "Cᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴄʟᴇᴀʀᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "Mᴇᴅɪᴀ ᴄʟᴇᴀʀᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ."
    
    SAVED_RECVD_DOC_FILE = "Dᴏᴡɴʟᴏᴀᴅᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "Nᴏ Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ ғᴏᴜɴᴅ."
    
    NO_VOID_FORMAT_FOUND = "ɴᴏ-ᴏɴᴇ ɢᴏɴɴᴀ ʜᴇʟᴘ ʏᴏᴜ\n{}"
    
    USER_ADDED_TO_DB = "Usᴇʀ <a href='tg://user?id={}'>{}</a> ᴀᴅᴅᴇᴅ ᴛᴏ {} ᴛɪʟʟ {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "Aʟʀᴇᴀᴅʏ ᴀ ᴘʀᴏᴄᴇss ɢᴏɪɴɢ ᴏɴ!!!\n\nCʜᴇᴄᴋ Lɪᴠᴇ Sᴛᴀᴛᴜs ᴏɴ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ."
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "Hi, I am Video Compressor Bot \n\n1. Send me your telegram big video file \n2. Reply to the file with: `/compress 50` \n\nSupport Group: @ParadoxChats"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
