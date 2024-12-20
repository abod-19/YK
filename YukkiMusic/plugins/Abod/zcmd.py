from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, CallbackQuery, InlineKeyboardMarkup
from YukkiMusic import app
from config import CHANNEL_LINK, CHANNEL_NAME, OWNER_ID
from YukkiMusic.misc import SUDOERS

lnk = "https://t.me/" + CHANNEL_LINK

@app.on_callback_query(filters.regex("aprvett"))
async def prvett(_, query: CallbackQuery):
    await query.edit_message_text(
            f"""- اهلين فيـك عمـري في بوت {app.mention} ♪

- وضيفة البوت تشغيل الوسائط والاغاني في المكالمات الجماعية الخاصة بالمجوعات والقنوات

- لعـرض كيبـورد الاوامـر الخـدميـة إضغـط ← /cmds""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("الاوامــر", callback_data="prvett")
                    ],[
                        InlineKeyboardButton("المطور", url=f"tg://openmessage?user_id={OWNER_ID[0]}"),
                    ],[
                        InlineKeyboardButton(text=CHANNEL_NAME, url=lnk)
                    ],[
                        InlineKeyboardButton("اضفني قروبك", url=f"https://t.me/{app.username}?startgroup=true"),
                    ],
                ]
            ),
        )


@app.on_callback_query(filters.regex("azzzback"))
async def prvett(_, query: CallbackQuery):
    await query.edit_message_text(
            """- اليك اوامر الميوزك .
        
- استخدم الازرار الي تحت .""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("اوامــر التشغيــل", callback_data="azzzll")],
                    [
                        InlineKeyboardButton("اوامـر القنـاة", callback_data="azzzch"),
                        InlineKeyboardButton("اوامـر الادمـن", callback_data="azzzad"),
                    ],
                    [InlineKeyboardButton("اوامــر المطــور", callback_data="azzzdv")],
                    [InlineKeyboardButton(text=CHANNEL_NAME, url=lnk)],
                    [InlineKeyboardButton("رجـوع", callback_data="aprvett")],
                ]
            ),
        )
    

@app.on_callback_query(filters.regex("azzzdv") & SUDOERS)
async def mpdtsf(_, query: CallbackQuery):
    await query.edit_message_text(
        """<b>- مرحبـاً بك عـزيـزي المطـور </b>\n\n<b>- استخدم الازرار الي تحت .\n- عشان تشوف اوامر الميوزك يعيني .</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("التحـديث", callback_data="azzzup")],
                [
                    InlineKeyboardButton("الـرفــع", callback_data="azzzsu"),
                    InlineKeyboardButton("الـحظــر", callback_data="azzzbn"),
                ],
                [InlineKeyboardButton("الاشعــارات & المسـاعــد", callback_data="azzzas")],
                [InlineKeyboardButton("رجـوع", callback_data="azzzback")],
            ]
        ),
    )

# تابع بقية الدوال باستخدام نفس الأسلوب لتنظيم الكود

@app.on_callback_query(filters.regex("azzzll"))
async def zzzll(_, query: CallbackQuery):
    await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر الـتشغـيـل :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
تشغيل + (اسم الاغنية / رابط الاغنية)
<b>- لــ تـشـغـيل اغـنـيـة فـي الـمكـالـمـة الـصـوتـيـة</b>

بحث + الاسـم
<b>- لـ تحميـل الاغانـي والمقـاطـع الصوتيـه مـن اليوتيـوب</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="azzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("azzzad"))
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

/الاغاني
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
                        "رجـوع", callback_data="azzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("azzzch"))
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
                        "رجـوع", callback_data="azzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("azzzup") & SUDOERS)
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
                        "رجـوع", callback_data="azzzdv"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("azzzsu") & SUDOERS)
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
                        "رجـوع", callback_data="azzzdv"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("azzzbn") & SUDOERS)
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
                        "رجـوع", callback_data="azzzdv"),
               ],
          ]
        ),
    )


@app.on_callback_query(filters.regex("azzzas") & SUDOERS)
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
                        "رجـوع", callback_data="azzzdv"),
               ],
          ]
        ),
   )
