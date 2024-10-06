import os, asyncio
import requests
from typing import Optional
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from YukkiMusic import app
from strings.filters import command

#---------------FUNCTION---------------#

def get_file_id(msg: Message) -> Optional[Message]:
    if not msg.media:
        return None

    for message_type in ("photo", "animation", "audio", "document", "video", "video_note", "voice", "sticker"):
        obj = getattr(msg, message_type)
        if obj:
            setattr(obj, "message_type", message_type)
            return obj

#---------------FUNCTION---------------#

@app.on_message(filters.regex(r"^(تلغراف|ميديا|تلكراف|تلجراف|‹ تلغراف ›)$") & filters.private)
async def cloud_upload(bot, update):
    replied = update.reply_to_message
    if not replied:
        return await update.reply_text("⌯ ¦ قم بالرد على ملف وسائط مدعوم.\n⌯ ¦ حط صوره او فيديو و اكتب عليها.")
    
    file_info = get_file_id(replied)
    if not file_info:
        return await update.reply_text("⌯ ¦ ياغبي غير مدعوم.\n⌯ ¦ حط صوره و اكتب عليها.")
    
    text = await update.reply_text(text="<code>انتظر يتم التحميل ...</code>", disable_web_page_preview=True)   
    media = await update.reply_to_message.download()   
    
    await text.edit_text(text="<code>اكتمل التحميل. الآن يتم رفعه إلى envs.sh ...</code>", disable_web_page_preview=True)                                            
    try:
        # رفع الملف إلى envs.sh
        with open(media, "rb") as f:
            data = f.read()
            resp = requests.post("https://envs.sh", files={"file": data})
        
        if resp.status_code == 200:
            upload_url = f"{resp.text}"
        else:
            await text.edit_text("حدث خطأ أثناء الرفع إلى envs.sh. حاول مرة أخرى لاحقاً.")
            return
    except Exception as error:
        print(error)
        await text.edit_text(text=f"Error :- {error}", disable_web_page_preview=True)       
        return    
    finally:
        try:
            os.remove(media)
        except Exception as error:
            print(error)

    await text.edit_text(
        text=f"<b>⎉╎الــرابـط :</b> {upload_url}",
        disable_web_page_preview=False,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton(text="✘ اغلاق ✘", callback_data="close")
        ]])
    )

@app.on_callback_query(filters.regex("close"))
async def close_button(_, query: CallbackQuery):
    await query.message.delete()
