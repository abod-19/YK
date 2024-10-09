import asyncio
from pyrogram import Client, filters
from datetime import datetime
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton, Message
from YukkiMusic import app
from config import OWNER_ID
import os

@app.on_message(filters.member_joined)
async def get_chat_info(client, message):
    chat = await app.get_chat(message.chat.id)
    chat_name = chat.title  # اسم الجروب
    first_name = message.from_user.first_name  # اسم المستخدم
    username = message.from_user.username  # يوزر المستخدم
    join_time = datetime.now().strftime("%H:%M:%S")  # الوقت الحالي
    join_date = datetime.now().strftime("%Y-%m-%d")  # التاريخ الحالي
    
    await message.reply_text(f"""
𝐰𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐭𝐡𝐞 𝐠𝐫𝐨𝐮𝐩.🧸

__#{chat_name}___

➥• Welcome  : {first_name} 
➥• User : @{username if username else 'No username'}  
➥• time : {join_time}
➥• date : {join_date}
""")
