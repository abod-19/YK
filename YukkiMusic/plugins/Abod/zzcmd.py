from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, CallbackQuery, InlineKeyboardMarkup
from YukkiMusic import app
from config import CHANNEL_LINK, CHANNEL_NAME, OWNER_ID
from YukkiMusic.misc import SUDOERS

lnk = "https://t.me/" + CHANNEL_LINK


@app.on_callback_query(filters.regex("zzzback"))
async def zzzback(_, query: CallbackQuery):
    await query.edit_message_text(
        """<b>⟡ منور يحبي باوامر الميوزك .</b>\n\n<b>⟡ استخدم الازرار الي تحت .\n⟡ عشان تشوف اوامر الميوزك يعيني .</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("اوامــر التشغيــل", callback_data="zzzll")],
                [
                    InlineKeyboardButton("اوامـر القنـاة", callback_data="zzzch"),
                    InlineKeyboardButton("اوامـر الادمـن", callback_data="zzzad"),
                ],
                [InlineKeyboardButton("اوامــر المطــور", callback_data="zzzdv")],
                [InlineKeyboardButton(text=CHANNEL_NAME, url=lnk)],
            ]
        ),
    )
    

@app.on_callback_query(filters.regex("zzzdv") & SUDOERS)
async def mpdtsf(_, query: CallbackQuery):
    await query.edit_message_text(
        """<b>⟡ مرحبـاً بك عـزيـزي المطـور </b>\n\n<b>⟡ استخدم الازرار الي تحت .\n⟡ عشان تشوف اوامر الميوزك يعيني .</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("التحـديث", callback_data="zzzup")],
                [
                    InlineKeyboardButton("الـرفــع", callback_data="zzzsu"),
                    InlineKeyboardButton("الـحظــر", callback_data="zzzbn"),
                ],
                [InlineKeyboardButton("الاشعــارات & المسـاعــد", callback_data="zzzas")],
                [InlineKeyboardButton("رجـوع", callback_data="zzzback")],
            ]
        ),
    )

# تابع بقية الدوال باستخدام نفس الأسلوب لتنظيم الكود

@app.on_callback_query(filters.regex("zzzll"))
async def zzzll(_, query: CallbackQuery):
    await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر الـتشغـيـل :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
تشغيل + (اسم المقطع / رابط المقطع)
<b>- لــ تـشـغـيل المقطع فـي الـمكـالـمـة الـصـوتـيـة</b>

فيديو + (اسم المقطع / رابط المقطع)
<b>- لــ تـشـغـيل المقطع فيديو فـي الـمكـالـمـة </b>


بحث + الاسـم
<b>- لـ تحميـل المقـاطـع الصوتيـه مـن اليوتيـوب</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzad"))
async def zzzad(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر الادمــن :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

الاعدادات
<b>- لـ عـرض إعـدادات اوضـاع التشغيـل</b>

ايقاف / اسكت
<b>- لـ إيقـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة</b>

وقف / توقف
<b>- لـ إيقـاف تشغيـل الموسيـقـى فـي المكالمـة مـؤقتـاً</b>

كمل / استئناف
<b>- لـ إسـتـئـنـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة</b>

تخطي / التالي
<b>- لـ تخطـي الاغنيـة وتشغيـل الاغنيـة التاليـه</b>

الاغاني
<b>- لـ معـرفـة الاغـانـي المـوجـودة فـي قائمـة الانتظـار</b>

بنج
<b>- لـ عـرض سـرعـة تشغيـل البـوت</b>

رفع ادمن/تنزيل ادمن
<b>- لـ رفـع/تنزيـل ادمـن فـي البـوت</b>

الادمنيه
<b>- لـ عـرض قائمـة ادمنيـة البـوت</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
/seek + عـدد الثـوانـي
<b>- لـ تقديـم الاغنيـه لـ الامـام</b>
/seekback + عـدد الثـوانـي
<b>- لـ إرجـاع الاغنيـه لـ الخـلف</b>
""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzch"))
async def zzzch(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر التشغيــل فـي القنــاة :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- ارفـع البـوت إشـراف في القنـاة و شغـل المكالمه</b>
<b>- انشاء مجموعه وارفع البوت اشراف</b>
<b>- ارسـل في المجموعه (/channelplay او /ربط) + يـوزر القنـاة لـ الربـط</b>
<b>- ثم استخـدم الاوامــر بالاسفـل بالمجموعه لـ التشغيـل</b>
<b>- "استخدم الاوامر بـ / او بدون"</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
/cplay + اسم الاغنية
<b>- لــ تـشـغـيل اغـنـيـة فـي الـمكـالـمـة الـصـوتـيـة</b>

/cvplay + اسم المقـطـع
<b>- لــ تـشـغـيل فيـديـو فـي الـمكـالـمـة المـرئيـة</b>

/cstop
<b>- لـ إيقـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة</b>

/cpause
<b>- لـ إيقـاف تشغيـل الموسيـقـى فـي المكالمـة مـؤقتـاً</b>

/cresume
<b>- لـ إسـتـئـنـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة</b>

/cskip
<b>- لـ تخطـي الاغنيـة وتشغيـل الاغنيـة التاليـه</b>
""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzup") & SUDOERS)
async def zzzup(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر المطــور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمــة اوامــر التحـديثـات :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

/السجلات
<b>- لـ جلب سجـلات البـوت 📋</b>

/تحديث
<b>- لـ تحديـث البــوت</b>

/اعاده تشغيل
<b>- لـ اعـادة تشغيـل البــوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzsu") & SUDOERS)
async def zzzsu(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر المطــور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمــة اوامــر الـرفــع :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>ملاحظه :- استخدم "/" قبل الامر</b>

رفع مطور/تنزيل مطور
<b>- لـ رفـع/تنزيـل شخـص مطـور فـي ميـوزك البـوت</b>

المطورين
<b>- لـ عـرض قائمـة مطـورين البـوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzbn") & SUDOERS)
async def zzzbn(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر المطــور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمــة اوامــر الحظــر :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>ملاحظه :- استخدم "/" قبل الامر</b>

حظر/الغاء الحظر
<b>- لـ حظـر/الغـاء حظـر شخـص من استخـدام ميـوزك البـوت</b>

المحظورين
<b>- لـ عـرض قائمـة المحظورين</b>

حظر عام/الغاء حظر عام
<b>- لـ حظـر/الغـاء حظـر شخـص من استخـدام ميـوزك البـوت عـام</b>

المحظورين عام
<b>- لـ جلب قائمـة المحظـورين عـام فـي البـوت</b>

حظر مجموعة/سماح
<b>- لـ حظـر/الغـاء حظـر مجموعـة من استخـدام ميـوزك البـوت</b>

المجموعات المحظورة
<b>- لـ جلب قائمـة بالمجمـوعـات المحظـورة مـن استـخـدام البـوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )


@app.on_callback_query(filters.regex("zzzas") & SUDOERS)
async def zzzas(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر المطــور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمــة اوامــر المســاعــد ✅ :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

السجل [ تفعيل / تعطيل ]
<b>- لـ تفعيـل/تعطيـل اشعـارات مجموعـة سجـل البــوت</b>

مغادره تفعيل/تعطيل
<b>- لـ تفعيـل/تعطيـل المغـادره التلقائيـه لـ الحسـاب المسـاعـد مـن المجمـوعـات عنـد عـدم استـخـدام الميـوزك</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzdv"),
               ],
          ]
        ),
   )
