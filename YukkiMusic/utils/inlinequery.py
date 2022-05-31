#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Pause Stream",
            description=f"Pause the current playout on group call.",
            thumb_url="https://telegra.ph/file/c0a1c789def7b93f13745.png",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="Resume Stream",
            description=f"Resume the ongoing playout on group call.",
            thumb_url="https://telegra.ph/file/02d1b7f967ca11404455a.png",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="Mute Stream",
            description=f"Mute the ongoing playout on group call.",
            thumb_url="https://telegra.ph/file/66516f2976cb6d87e20f9.png",
            input_message_content=InputTextMessageContent("/mute"),
        ),
        InlineQueryResultArticle(
            title="Unmute Stream",
            description=f"Unmute the ongoing playout on group call.",
            thumb_url="https://telegra.ph/file/3078794f9341ffd582e18.png",
            input_message_content=InputTextMessageContent("/unmute"),
        ),
        InlineQueryResultArticle(
            title="Skip Stream",
            description=f"Skip to next track. | For Specific track number: /skip [number] ",
            thumb_url="https://telegra.ph/Skip-05-31",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="End Stream",
            description="Stop the ongoing playout on group call.",
            thumb_url="https://telegra.ph/Stop-05-31",
            input_message_content=InputTextMessageContent("/stop"),
        ),
        InlineQueryResultArticle(
            title="Shuffle Stream",
            description="Shuffle the queued tracks list.",
            thumb_url="https://telegra.ph/Shuffle-05-31",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="Seek Stream",
            description="Seek the ongoing stream to a specific duration.",
            thumb_url="https://telegra.ph/Loop-05-30-2",
            input_message_content=InputTextMessageContent("/seek 10"),
        ),
        InlineQueryResultArticle(
            title="Loop Stream",
            description="Loop the current playing music. | Usage: /loop [enable|disable]",
            thumb_url="https://telegra.ph/Loop-05-31
",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
