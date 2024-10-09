import asyncio
from pyrogram import Client, filters
from datetime import datetime
from YukkiMusic import app

@app.on_message(filters.new_chat_members)
async def welcome_new_member(client: Client, message):
    chat = await app.get_chat(message.chat.id)
    chat_name = chat.title  # اسم الجروب
    chat_photo = chat.photo  # صورة الجروب
    for new_member in message.new_chat_members:
        first_name = new_member.first_name  # اسم العضو الجديد
        username = new_member.username  # يوزر العضو الجديد
        user_id = new_member.id  # آيدي العضو الجديد
        join_time = datetime.now().strftime("%I:%M %p")  # الوقت بصيغة 12 ساعة مع AM/PM
        join_date = datetime.now().strftime("%Y/%m/%d")  # التاريخ بصيغة / 

        # إنشاء النص الترحيبي بتنسيق مشابه للصورة
        welcome_text = f"""
═WELCOME TO {chat_name} GROUP═

°•--------D i o r--------•°

✨🥂  نورت قروبنا   『{first_name}』  🥂✨
        
        • اسمك  ➠ 『{first_name}』
        • آيديك  ➠ 『{user_id}』
        • يوزرك ➠ {'@' + username if username else 'لا يوجد يوزر'}

°•--------D i o r--------•°

      ⌜تاريخ انضمامك⌝   ➠ 『{join_date}』
      ⌜الساعة⌝   ➠ 『{join_time}』
"""

        # التحقق إذا كانت المجموعة تحتوي على صورة
        if chat_photo:
            # تنزيل الصورة وحفظها
            photo_file = await client.download_media(chat_photo.big_file_id)

            # إرسال الصورة مع النص
            await message.reply_photo(
                photo=photo_file,  # استخدام مسار الصورة التي تم تنزيلها
                caption=welcome_text
            )
        else:
            # إرسال النص فقط إذا لم تكن هناك صورة
            await message.reply_text(welcome_text)
