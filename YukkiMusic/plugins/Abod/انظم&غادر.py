from pyrogram import filters
from pyrogram.errors import ChatAdminRequired, InviteRequestSent, UserAlreadyParticipant
from strings.filters import command
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.database import get_assistant
from pyrogram.types import Message 
import config

Nem = config.BOT_NAME + " غادر"

@app.on_message(
    command(["المساعد انضم","انضمام المساعد","مساعد انضم"]))
async def invite_assistant(client, message):
    try:
        userbot = await get_assistant(message.chat.id)
        try:
            await client.get_chat_member(message.chat.id, "me")
        except ChatAdminRequired:
            return await message.reply_text("-› اعطيني صلاحية اضافة مستخدمين .")
        try:
            await client.unban_chat_member(message.chat.id, userbot.id)
        except:
            pass
            
        invitelink = await client.export_chat_invite_link(message.chat.id)
        await userbot.join_chat(invitelink)
        await message.reply_text("-› تمت اضافة المساعد بنجاح .")

    except InviteRequestSent:
        await message.reply_text("-› بالفعل تم دعوة المساعد .")

    except UserAlreadyParticipant:
        await message.reply_text("-› ترى المساعد موجود .")

    except Exception as e:
        await message.reply_text(f"-› حدث خطأ .: {e}")
        

@app.on_message(command(["المساعد غادر", "مساعد غادر", "مساعد مغادره"]) & SUDOERS)
async def leave_group(client, message):
    try:
        userbot = await get_assistant(message.chat.id)

        if not await userbot.get_chat_member(message.chat.id, userbot.me.id):
            await message.reply_text("-› المساعد مغادر من قبل.")
            return
        
        await userbot.leave_chat(message.chat.id)
        await message.reply_text("-› غادر المساعد كما طلبت.")

    except Exception as e:
        if "USER_NOT_PARTICIPANT" in str(e):
            await message.reply_text("-› المساعد مغادر من قبل.")
        else:
            await message.reply_text(f"-› حدث خطأ أثناء مغادرة المجموعة: {e}")



@app.on_message(command([Nem]) & filters.user(config.OWNER_ID[0]))
async def leave_group(client, message):
    try:
        userbot = await get_assistant(message.chat.id)
        leave_message = "-› شكرًا لكم جميعًا، وداعاً!"
        await app.send_message(message.chat.id, leave_message)
        await app.leave_chat(message.chat.id)
        await userbot.leave_chat(message.chat.id)

        await message.reply_text("-› غادرت المجموعة كما طلبت.")

    except Exception as e:
        await message.reply_text(f"-› حدث خطأ أثناء مغادرة المجموعة: {e}")
