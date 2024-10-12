import asyncio
from pyrogram import Client, filters
from datetime import datetime, timedelta
from YukkiMusic import app
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@app.on_message(filters.new_chat_members)
async def welcome_new_member(client: Client, message):
    chat = await app.get_chat(message.chat.id)
    chat_name = chat.title  # اسم الجروب
    chat_photo = chat.photo  # صورة الجروب
    
    chat_id = message.chat.id
    async for member in client.get_chat_members(chat_id):
        if member.status == ChatMemberStatus.OWNER:  # جلب منشئ المجموعة فقط
            owner_id = member.user.id
            owner_name = member.user.first_name
     
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[
                InlineKeyboardButton(f"{owner_name}", url=f"tg://openmessage?user_id={owner_id}")
            ]]
    )       
    for new_member in message.new_chat_members:
        first_name = new_member.mention  # اسم العضو الجديد
        username = new_member.username  # يوزر العضو الجديد
        # الحصول على الوقت الحالي
        now = datetime.utcnow()  # استخدام الوقت العالمي UTC
        # تعديل الوقت ليصبح حسب التوقيت اليمني (UTC +3)
        yemen_time = now + timedelta(hours=3)

        # تنسيق الوقت والتاريخ
        join_time = yemen_time.strftime("%I:%M %p")  # الوقت بصيغة 12 ساعة مع AM/PM
        join_date = yemen_time.strftime("%Y/%m/%d")  # التاريخ بصيغة YYYY/MM/DD

        # إنشاء النص الترحيبي
        welcome_text = f"""
𝐰𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐭𝐡𝐞 𝐠𝐫𝐨𝐮𝐩.🧸

__{chat_name}__

➥• Welcome  : {first_name} 
➥• User : @{username if username else 'No username'}  
➥• time : {join_time}
➥• date : {join_date}
"""
        # التحقق إذا كانت المجموعة تحتوي على صورة
        if chat_photo:
            # تنزيل الصورة وحفظها
            photo_file = await client.download_media(chat_photo.big_file_id)

            # إرسال الصورة مع النص
            await message.reply_photo(
                photo=photo_file,  # استخدام مسار الصورة التي تم تنزيلها
                caption=welcome_text,
                reply_markup=keyboard
            )
        else:
            # إرسال النص فقط إذا لم تكن هناك صورة
            await message.reply_text(welcome_text, reply_markup=keyboard)


@app.on_message(filters.left_chat_member)
async def leftmem(client, message):
    chat = await app.get_chat(message.chat.id)
    gti = chat.title
    link = await app.export_chat_invite_link(message.chat.id)

    user_id = message.left_chat_member.id

    chat_id = message.chat.id
    async for member in client.get_chat_members(chat_id):
        if member.status == ChatMemberStatus.OWNER:  # جلب منشئ المجموعة فقط
            owner_id = member.user.id
            owner_name = member.user.first_name

    buttons = [
        [
            InlineKeyboardButton(f"{owner_name}", url=f"tg://openmessage?user_id={owner_id}")
        ],[
            InlineKeyboardButton(gti, url=f"{link}")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await app.send_message(user_id, f"<b>• في امان الله ياعيوني يا 〖 {message.left_chat_member.mention} ⁪⁬⁮⁮⁮⁮〗.\n</b>"
                                    f"<b>• اذا فكرت ترجع قروبنا {gti}\n</b>"
                                    f"<b>• اذا كان سبب مغادرتك ازعاج من مشرف\n</b>"
                                    f"<b>• يمكنك تقديم شكوه للمالك  والرجوع للجروب\n</b>"
                                    f"<b>• من خلال الازرار بالاسفل 🧚🏻‍♀️</b>"
                                    f"<a href='{link}'>ㅤ</a>",
                                    reply_markup=reply_markup)
    
