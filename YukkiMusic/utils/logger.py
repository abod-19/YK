#
# Copyright (C) 2024 by TheTeamVivek@Github, < https://github.com/TheTeamVivek >.
#
# This file is part of < https://github.com/TheTeamVivek/YukkiMusic > project,
# and is released under the MIT License.
# Please see < https://github.com/TheTeamVivek/YukkiMusic/blob/master/LICENSE >
#
# All rights reserved.

from config import LOG, LOG_GROUP_ID
from YukkiMusic import app
from YukkiMusic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.from_user:
            ne = "تم التشغيل في المجموعة"
            user_id = message.from_user.id
            user_mention = message.from_user.mention
            user_username = message.from_user.username
        else:
            ne = "تم التشغيل في القناة"
            user_id = "مجهول"
            user_mention = "مجهول"
            user_username = "مجهول"
        logger_text = f"""
<b>{ne}</b>

<b>شات ايدي :</b> <code>{message.chat.id}</code>
<b>الاسم :</b> {message.chat.title}
<b>اليوزر :</b> @{message.chat.username}

<b>ايدي :</b> <code>{user_id}</code>
<b>الاسم :</b> {user_mention}
<b>يوزر :</b> @{user_username}

<b>الاغنيه :</b> {message.text.split(None, 1)[1]}
<b>اسم المشغل :</b> {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    chat_id=LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except Exception as e:
                print(e)
        return
