import asyncio
from pyrogram import Client, filters
from datetime import datetime
from YukkiMusic import app

@app.on_message(filters.new_chat_members)
async def welcome_new_member(client: Client, message):
    chat = await app.get_chat(message.chat.id)
    chat_name = chat.title  # اسم الجروب
    for new_member in message.new_chat_members:
        first_name = new_member.first_name  # اسم العضو الجديد
        username = new_member.username  # يوزر العضو الجديد
        join_time = datetime.now().strftime("%H:%M:%S")  # الوقت الحالي
        join_date = datetime.now().strftime("%Y-%m-%d")  # التاريخ الحالي

        # إرسال رسالة ترحيب
        await message.reply_text(f"""
𝐰𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐭𝐡𝐞 𝐠𝐫𝐨𝐮𝐩.🧸

__#{chat_name}___

➥• Welcome  : {first_name} 
➥• User : @{username if username else 'No username'}  
➥• time : {join_time}
➥• date : {join_date}
""")
