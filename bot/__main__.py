from datetime import datetime as dt
import os, asyncio, pyrogram, psutil, platform
from bot import (
    APP_ID,
    API_HASH,
    AUTH_USERS,
    DOWNLOAD_LOCATION,
    LOGGER,
    TG_BOT_TOKEN,
    BOT_USERNAME,
    SESSION_NAME,
    
    data,
    app,
    crf,
    resolution,
    audio_b,
    preset,
    codec,
    watermark 
)
from bot.helper_funcs.utils import add_task, on_task_complete, sysinfo
from pyrogram import Client, filters, enums
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from pyrogram.types import Message
from psutil import disk_usage, cpu_percent, virtual_memory, Process as psprocess
from flask import Flask

from bot.plugins.incoming_message_fn import (
    incoming_start_message_f,
    incoming_compress_message_f,
    incoming_cancel_message_f
)


from bot.plugins.status_message_fn import (
    eval_message_f,
    exec_message_f,
    upload_log_file
)

from bot.commands import Command
from bot.plugins.call_back_button_handler import button
sudo_users = "7086472788 1136967391" 
crf.append("27")
codec.append("libx264")
resolution.append("1920x1080")
preset.append("superfast")
audio_b.append("35k")

uptime = dt.now()

def ts(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + "d, ") if days else "")
        + ((str(hours) + "h, ") if hours else "")
        + ((str(minutes) + "m, ") if minutes else "")
        + ((str(seconds) + "s, ") if seconds else "")
        + ((str(milliseconds) + "ms, ") if milliseconds else "")
    )
    return tmp[:-2]

# Create a Flask app
web_app = Flask(__name__)

# Define a health check route
@web_app.route('/health', methods=['GET'])
def health_check():
    return "OK", 200  # Respond with a 200 OK status to indicate the service is healthy

if __name__ == "__main__":
    # Run the Flask app on port 8080
    from threading import Thread
    def run_web_app():
        web_app.run(host="0.0.0.0", port=8080)

    # Start the Flask web app in a separate thread so it runs alongside the Pyrogram bot
    Thread(target=run_web_app).start()


if __name__ == "__main__" :
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)
    
    
    app.set_parse_mode(enums.ParseMode.MARKDOWN)

    incoming_start_message_handler = MessageHandler(
        incoming_start_message_f,
        filters=filters.command(["start", f"start@{BOT_USERNAME}"])
    )
    app.add_handler(incoming_start_message_handler)
    
    
    @app.on_message(filters.incoming & filters.command(["crf", f"crf@{BOT_USERNAME}"]))
    async def changecrf(app, message):
        if message.from_user.id in AUTH_USERS:
            cr = message.text.split(" ", maxsplit=1)[1]
            OUT = f"I Wɪʟʟ ʙᴇ ᴜsɪɴɢ: {cr} Cʀғ"
            crf.insert(0, f"{cr}")
            await message.reply_text(OUT)
        else:
            await message.reply_text("Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴅᴏ ᴛʜɪs.")
            
    @app.on_message(filters.incoming & filters.command(["settings", f"settings@{BOT_USERNAME}"]))
    async def settings(app, message):
        if message.from_user.id in AUTH_USERS:
            await message.reply_text(f"Cᴜʀʀᴇɴᴛ sᴇᴛᴛɪɴɢs ғᴏʀ ᴛʜᴇ ᴠɪᴅᴇᴏ ᴇɴᴄᴏᴅɪɴɢ::\n\nCᴏᴅᴇᴄ: {codec[0]} \nCʀғ: {crf[0]} \nRᴇsᴏʟᴜᴛɪᴏɴ: {resolution[0]} \nᴘʀᴇsᴇᴛ: {preset[0]} \nᴀᴜᴅɪᴏ Bɪᴛʀᴀᴛᴇ: {audio_b[0]}")
        else:
            await message.reply_text("Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴅᴏ ᴛʜɪs.")

    @app.on_message(filters.incoming & filters.command(["sysinfo", f"sysinfo@{BOT_USERNAME}"]))
    async def help_message(app, message):
       if message.from_user.id in AUTH_USERS:
           await sysinfo(message)
       else:
           await message.reply_text("Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴅᴏ ᴛʜɪs.")
               
    @app.on_message(filters.incoming & filters.command(["resolution", f"resolution@{BOT_USERNAME}"]))
    async def changer(app, message):
        if message.from_user.id in AUTH_USERS:
            r = message.text.split(" ", maxsplit=1)[1]
            OUT = f"I Wɪʟʟ ʙᴇ ᴜsɪɴɢ: {r} ʀᴇsᴏʟᴜᴛɪᴏɴ"
            resolution.insert(0, f"{r}")
            await message.reply_text(OUT)
        else:
            await message.reply_text("Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴅᴏ ᴛʜɪs.")

            
               
    @app.on_message(filters.incoming & filters.command(["preset", f"preset@{BOT_USERNAME}"]))
    async def changepr(app, message):
        if message.from_user.id in AUTH_USERS:
            pop = message.text.split(" ", maxsplit=1)[1]
            OUT = f"I Wɪʟʟ ʙᴇ ᴜsɪɴɢ: {pop} ᴘʀᴇsᴇᴛ"
            preset.insert(0, f"{pop}")
            await message.reply_text(OUT)
        else:
            await message.reply_text("Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴅᴏ ᴛʜɪs.")

            
    @app.on_message(filters.incoming & filters.command(["codec", f"codec@{BOT_USERNAME}"]))
    async def changecode(app, message):
        if message.from_user.id in AUTH_USERS:
            col = message.text.split(" ", maxsplit=1)[1]
            OUT = f"I Wɪʟʟ ʙᴇ ᴜsɪɴɢ: {col} ᴄᴏᴅᴇᴄ"
            codec.insert(0, f"{col}")
            await message.reply_text(OUT)
        else:
            await message.reply_text("Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴅᴏ ᴛʜɪs.")
             
    @app.on_message(filters.incoming & filters.command(["audio", f"audio@{BOT_USERNAME}"]))
    async def changea(app, message):
        if message.from_user.id in AUTH_USERS:
            aud = message.text.split(" ", maxsplit=1)[1]
            OUT = f"I Wɪʟʟ ʙᴇ ᴜsɪɴɢ: {aud} ᴀᴜᴅɪᴏ"
            audio_b.insert(0, f"{aud}")
            await message.reply_text(OUT)
        else:
            await message.reply_text("Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴅᴏ ᴛʜɪs.")
            
        
    @app.on_message(filters.incoming & filters.command(["compress", f"compress@{BOT_USERNAME}"]))
    async def help_message(app, message):
        if message.chat.id not in AUTH_USERS:
            return await message.reply_text("Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ...")
        query = await message.reply_text("Fɪʟᴇ Aᴅᴅᴇᴅ ᴛᴏ Qᴜᴇᴜᴇ...\n\nEɴᴄᴏᴅɪɴɢ ᴡɪʟʟ sᴛᴀʀᴛ sᴏᴏɴ...", quote=True)
        data.append(message.reply_to_message)
        if len(data) == 1:
         await query.delete()   
         await add_task(message.reply_to_message)     
 
    @app.on_message(filters.incoming & filters.command(["restart", f"restart@{BOT_USERNAME}"]))
    async def restarter(app, message):
        if message.from_user.id in AUTH_USERS:
            await message.reply_text("Rᴇsᴛᴀʀᴛɪɴɢ...")
            quit(1)
        else:
            await message.reply_text("Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴅᴏ ᴛʜɪs.")
            
    @app.on_message(filters.incoming & filters.command(["clear", f"clear@{BOT_USERNAME}"]))
    async def restarter(app, message):
        if message.from_user.id in AUTH_USERS:
            await message.reply_text("Sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʟᴇᴀʀᴇᴅ ǫᴜᴇᴜᴇᴅ ғɪʟᴇs...")
        else:
            await message.reply_text("Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴅᴏ ᴛʜɪs.")
         
        
    @app.on_message(filters.incoming & (filters.video | filters.document))
    async def help_message(app, message):
        if message.chat.id not in AUTH_USERS:
            return await message.reply_text("Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ...")
        query = await message.reply_text("Fɪʟᴇ Aᴅᴅᴇᴅ ᴛᴏ Qᴜᴇᴜᴇ...\n\nEɴᴄᴏᴅɪɴɢ ᴡɪʟʟ sᴛᴀʀᴛ sᴏᴏɴ...", quote=True)
        data.append(message)
        if len(data) == 1:
         await query.delete()   
         await add_task(message)
            
    @app.on_message(filters.incoming & (filters.photo))
    async def help_message(app, message):
        if message.chat.id not in AUTH_USERS:
            return await message.reply_text("Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ...")
        os.system('rm thumb.jpg')
        await message.download(file_name='thumb.jpg')
        await message.reply_text('Tʜᴜᴍʙɴᴀɪʟ Aᴅᴅᴇᴅ...')
        
    @app.on_message(filters.incoming & filters.command(["cancel", f"cancel@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await incoming_cancel_message_f(app, message)
        
        
    @app.on_message(filters.incoming & filters.command(["exec", f"exec@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await exec_message_f(app, message)
        
    @app.on_message(filters.incoming & filters.command(["eval", f"eval@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await eval_message_f(app, message)
        
    @app.on_message(filters.incoming & filters.command(["stop", f"stop@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await on_task_complete()    
   
    @app.on_message(filters.incoming & filters.command(["help", f"help@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await message.reply_text("Hɪ..., I ᴀᴍ **Sᴀsᴜᴋᴇ Uᴄʜɪʜᴀ**!\n\nI ᴄᴀɴ ᴇɴᴄᴏᴅᴇ ᴠɪᴅᴇᴏ ɪɴ ᴀɴʏ ᴄᴏᴅᴇᴄ (ᴇ.ɢ. ʟɪʙx264, ʟɪʙx265) ᴡɪᴛʜ ᴛʜᴇ ғᴀsᴛᴇʀ sᴇᴛᴛɪɴɢs ᴀʟʀᴇᴀᴅʏ ʙᴜɪʟᴛɪɴ.\n\nYᴏᴜ ᴄᴀɴ ᴇᴀsɪʟʏ ᴄʜᴀɴɢᴇ ᴍʏ sᴇᴛᴛɪɴɢs ᴛʜʀᴏᴜɢʜ ᴄᴏᴍᴍᴀɴᴅs.\n\n**Cᴏᴍᴍᴀɴᴅ Lɪsᴛ:**\n• `/start` - Cʜᴇᴄᴋ ɪғ ᴛʜᴇ ʙᴏᴛ ɪs ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ.\n• `/crf <value>` - Cʜᴀɴɢᴇ ᴛʜᴇ Cᴏɴsᴛᴀɴᴛ Rᴀᴛᴇ Fᴀᴄᴛᴏʀ (CRF) ғᴏʀ ᴇɴᴄᴏᴅɪɴɢ.\n• `/settings` - Vɪᴇᴡ ᴄᴜʀʀᴇɴᴛ ᴇɴᴄᴏᴅɪɴɢ sᴇᴛᴛɪɴɢs.\n• `/sysinfo` - Gᴇᴛ sʏsᴛᴇᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.\n• `/resolution <value>` - Cʜᴀɴɢᴇ ᴛʜᴇ ᴠɪᴅᴇᴏ ʀᴇsᴏʟᴜᴛɪᴏɴ.\n• `/preset <value>` - Cʜᴀɴɢᴇ ᴛʜᴇ ᴇɴᴄᴏᴅɪɴɢ ᴘʀᴇsᴇᴛ.\n• `/codec <value>` - Cʜᴀɴɢᴇ ᴛʜᴇ ᴠɪᴅᴇᴏ ᴄᴏᴅᴇᴄ.\n• `/audio <type>` - Cʜᴀɴɢᴇ ᴛʜᴇ ᴀᴜᴅɪᴏ ᴛʏᴘᴇ (ᴇ.ɢ., AAC).\n• `/compress` - Cᴏᴍᴘʀᴇss ᴀ ғɪʟᴇ ᴏʀ ᴀᴅᴅ ɪᴛ ᴛᴏ ᴛʜᴇ ǫᴜᴇᴜᴇ.\n• `/restart` - Rᴇsᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ.\n• `/clear` - Cʟᴇᴀʀ ᴛʜᴇ ᴘʀᴏᴄᴇssɪɴɢ ǫᴜᴇᴜᴇ.\n• `/cancel` - Cᴀɴᴄᴇʟ ᴛʜᴇ ʟᴀsᴛ ᴘʀᴏᴄᴇss.\n• `/eval <code>` - Gʀᴀɴᴛ ᴇᴠᴀʟᴜᴀᴛɪᴏɴ ᴀᴄᴄᴇss ᴛᴏ ᴀ ᴜsᴇʀ.\n• `/help` - Sʜᴏᴡ ᴛʜɪs ʜᴇʟᴘ ᴍᴇssᴀɢᴇ.\n• `/log` - Gᴇᴛ ᴛʜᴇ ʙᴏᴛ's ʟᴏɢs.\n• `/ping` - Cʜᴇᴄᴋ ᴛʜᴇ ʙᴏᴛ's ʀᴇsᴘᴏɴsɪᴠᴇɴᴇss.\n\nLᴇᴛ ᴍᴇ ʜᴀɴᴅʟᴇ ʏᴏᴜʀ ᴇɴᴄᴏᴅɪɴɢ ᴛᴀsᴋs ᴇғғɪᴄɪᴇɴᴛʟʏ. 🚀", quote=True)
  
    @app.on_message(filters.incoming & filters.command(["log", f"log@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await upload_log_file(app, message)
    @app.on_message(filters.incoming & filters.command(["ping", f"ping@{BOT_USERNAME}"]))
    async def up(app, message):
      stt = dt.now()
      ed = dt.now()
      v = ts(int((ed - uptime).seconds) * 1000)
      u = f"Bᴏᴛ Tᴏᴛᴀʟ Uᴘᴛɪᴍᴇ = {v}"
      ms = (ed - stt).microseconds / 1000
      p = f"Pɪɴɢ = {ms}ms"
      await message.reply_text(u + "\n" + p)

    call_back_button_handler = CallbackQueryHandler(
        button
    )
    app.add_handler(call_back_button_handler)

    # run the APPlication
    app.run()
