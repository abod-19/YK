from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus
from YukkiMusic import app


@app.on_message(filters.command(["المالك", "صاحب الخرابه", "المنشي"], ""))
async def gak_owne(client: Client, message: Message):
    chat_id = message.chat.id
    async for member in client.get_chat_members(chat_id):
        if member.status == ChatMemberStatus.OWNER:  # جلب منشئ المجموعة فقط
            owner_id = member.user.id
            owner_name = member.user.first_name
            return await message.reply(f"المالك : {owner_name}\nالايدي : {owner_id}")
        else:
          return
