#
# Copyright (C) 2024 by TheTeamVivek@Github, < https://github.com/TheTeamVivek >.
#
# This file is part of < https://github.com/TheTeamVivek/YukkiMusic > project,
# and is released under the MIT License.
# Please see < https://github.com/TheTeamVivek/YukkiMusic/blob/master/LICENSE >
#
# All rights reserved.
#
from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import CHANNEL_LINK, SUPPORT_CHANNEL, SUPPORT_GROUP, CHANNEL_NAME
from YukkiMusic import app

lnk= "https://t.me/" +CHANNEL_LINK

def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_B_2"], callback_data="settings_helper"),
        ],[
            InlineKeyboardButton(text="الأوامر", callback_data="zzzback")
        ]
    ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [InlineKeyboardButton(text="الأوامر", callback_data="prvett")]
    ]
    #buttons.append(
        #[
            #InlineKeyboardButton(
               # text=_["S_B_5"],
             #   url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
          #  )
       # ]
   # )
    if lnk and OWNER:
        buttons.append(
            [
                InlineKeyboardButton(text="المطور", user_id=OWNER),
                #InlineKeyboardButton(text=CHANNEL_NAME, url=lnk),
            ]
        )
        buttons.append(
            [
                #InlineKeyboardButton(text="المطور", user_id=OWNER),
                InlineKeyboardButton(text=CHANNEL_NAME, url=lnk),
            ]
        )
    else:

        if lnk:
            buttons.append(
                [
                    InlineKeyboardButton(text=CHANNEL_NAME, url=lnk),
                ]
            )

        if OWNER:
            buttons.append(
                [
                    InlineKeyboardButton(text="المطور", user_id=OWNER),
                ]
            )

    buttons.append(
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ]
    )
    return buttons


def alive_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✿︎ ᴀᴅᴅ ᴍᴇ ✿︎", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}"),
        ],
    ]
    return buttons
