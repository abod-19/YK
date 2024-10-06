from pyrogram import filters, Client
from ZeMusic import app
import asyncio
from pyrogram.types import VideoChatEnded, Message
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from ZeMusic.core.call import Mody
from ZeMusic.utils.database import *
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError,AlreadyJoinedError)

@app.on_message(filters.regex("^(مين في الكول|من في الكول|من بالمكالمه|من بالمكالمة|من في المكالمه|من في المكالمة|الصاعدين)$"))
async def strcall(client, message):
    assistant = await group_assistant(Mody,message.chat.id)
    try:
        await assistant.join_group_call(message.chat.id, AudioPiped("./ZeMusic/assets/call.mp3"), stream_type=StreamType().pulse_stream)
        text="<b>⟡ الموجودين في المكالمه :</b>\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="يتحدث"
            else:
                mut="يستمع"
            user = await client.get_users(participant.user_id)
            k +=1
            text +=f"{k} - {user.mention} : {mut}\n"
        text += f"\n<b>عددهم :</b> {len(participants)}"    
        await message.reply(f"{text}")
        await asyncio.sleep(7)
        await assistant.leave_group_call(message.chat.id)
    except NoActiveGroupCall:
        await message.reply(f"⟡ المكالمه مقفله يحلو")
    except TelegramServerError:
        await message.reply(f"⟡ حدث خطاء حاول مجدداً")
    except AlreadyJoinedError:
        text="<b>⟡ الموجودين في المكالمه :</b>\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="يتحدث"
            else:
                mut="يستمع"
            user = await client.get_users(participant.user_id)
            k +=1
            text +=f"{k} - {user.mention} : {mut}\n"
        text += f"\n<b>عددهم :</b> {len(participants)}"    
        await message.reply(f"{text}")
