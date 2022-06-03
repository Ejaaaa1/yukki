#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from config import LOG, LOG_GROUP_ID
from YukkiMusic import app
from YukkiMusic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(5):
            if message.chat.username:
                chatusername = f"@{message.chat.username}"
            else:
                chatusername = "Private Group"
            try:
                query = message.text.split(None, 1)[1]
                what = "Query Given"
            except:
                try:
                    if not message.reply_to_message:
                        what = "Command Given Only"
                    else:
                        what = "Replied to any file."
                except:
                    what = "Command"
            logger_text = f"""
__**New {what}**__
**Chat:** {message.chat.title} [`{message.chat.id}`]
**User:** {message.from_user.mention}
**Username:** @{message.from_user.username}
**User ID:** `{message.from_user.id}`
**Chat Link:** {chatusername}
**Query:** {message.text}"""
            if LOG_CLIENT != "None":
                await LOG_CLIENT.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
        return 
