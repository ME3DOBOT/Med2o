from pyrogram.types import CallbackQuery
#from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from pyrogram import Client 
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto


@app.on_message(
    filters.command("الاوامر", "")
)
async def cr_source(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5e62743deac646e4a2cdf.jpg",
        caption=f"""**⩹━⊷━⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝━⊶━⩺**\nمرحبا بك عزيزي {message.from_user.mention}\nهذا قسم الاوامر الخاص بسورس مـرعـب \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n**⩹━⊷━⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝━⊶━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامر الجروبات", callback_data="gr"),
                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data="ch"),  
                 ],[
                    InlineKeyboardButton(
                        "اوامر الادمن", callback_data="adm"), 
                ],[
                
                    InlineKeyboardButton(
                        "★⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝⚡", url=f"https://t.me/UC_IU"),
                ],

            ]

        ),

    )

    
@app.on_callback_query(filters.regex("gr"))
async def crusage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**⩹━⊷⌯⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝⌯⊶━⩺**
★¦ اهلا بك عزيزي في قسم اوامر التشغيل في الجروبات
★¦ تشغيل + اسم الاغنيه
★¦ فديو + اسم الاغنيه
★¦ #فيديو + اسم الاغنيه
★¦ #فديو + اسم الاغنيه
★¦ {NAME_BOT} + اسم الاغنيه
★¦ /فيديو + اسم الاغنيه
★¦ /ق شغل + اسم الاغنيه
★¦ /تشغيل + اسم الاغنيه
★¦ cvplay + اسم الاغنيه
★¦ cplay + اسم الاغنيه
★¦ /vplay + اسم الاغنيه
★¦ /play + اسم الاغنيه
★¦ #تشغيل + اسم الاغنيه
★¦ فيديو + اسم الاغنيه
★¦ سورة + اسم السورة 
★¦ cvplayforce + اسم الاغنيه
★¦ cplayforce + اسم الاغنيه
★¦ vplayforce + اسم الاغنيه
★¦ playforce + اسم الاغنيه
★¦ /cvplay + اسم الاغنيه
★¦ vplay + اسم الاغنيه
★¦ play + اسم الاغنيه

**⩹━⊷⌯⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝⌯⊶━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "التالي", callback_data="ch"), 
                    
                ],[
                    InlineKeyboardButton(
                        "الرئيسية", callback_data="back"), 
                    
                ]
            ]
        )
    )

@app.on_callback_query(filters.regex("ch"))
async def cr_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**⩹━⊷⌯⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝⌯⊶━⩺**
★¦ اهلا بك عزيزي في قسم اوامر التشغيل في القنوات
★¦ شغل + اسم الاغنيه
★¦ قناه + اسم الاغنيه
★¦ تشغيل + اسم الاغنيه
★¦ ق + اسم الاغنيه
★¦ اغاني + اسم الاغنيه
★¦ . + اسم الاغنيه
★¦ / + اسم الاغنيه
**⩹━⊷⌯⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝⌯⊶━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "التالي", callback_data="adm"), 
                    InlineKeyboardButton(
                        "العودة", callback_data="gr"), 
                ],[
                    InlineKeyboardButton(
                        "الرئيسية", callback_data="back"), 
                    
                ]
            ]
        )
    )

@app.on_callback_query(filters.regex("adm"))
async def c_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**⩹━⊷⌯⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝⌯⊶━⩺**
★¦ اهلا بك عزيزي في قسم اوامر تشغيل الادمن
★¦ رفع ثانوي
★¦ تنزيل ثانوي
★¦ قائمة الثانويين
★¦ حظر
★¦ الغاء الحظر
★¦ المحظورين
★¦ حظر عام
★¦ الغاء الحظر العام
★¦ المحظورين عام
★¦ اونلاين
★¦ اذاعه
★¦ تحديث
★¦ ريلود
★¦ وقف
★¦ كمل
★¦ اسكت
★¦ اتكلم
★¦ ايقاف
★¦ تخطي
★¦ @all
★¦ all stop
★¦ يوتيوب / تنزيل
★¦ تحديث
★¦ الاحصائيات
★¦ لايف
★¦ الاعدادت
★¦ بينج

**⩹━⊷⌯⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝⌯⊶━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "التالي", callback_data="gr"), 
                    InlineKeyboardButton(
                        "العودة", callback_data="ch"), 
                ],[
                    InlineKeyboardButton(
                        "الرئيسية", callback_data="back"), 
                    
                ]
            ]
        )
    )

    
@app.on_callback_query(filters.regex("back"))
async def cr_back(_, callback_query: CallbackQuery):
    await callback_query.edit_message_media(
        media=InputMediaPhoto("https://telegra.ph/file/c5952790fa8235f499749.jpg",
        caption=f"""**⩹━⊷━⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝━⊶━⩺**\nمرحبا بك عزيزي {callback_query.from_user.mention}\nهذا قسم الاوامر الخاص بسورس مـرعـب \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n**⩹━⊷━⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝━⊶━⩺**""",),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامر الجروبات", callback_data="gr"),
                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data="ch"),  
                 ],[
                    InlineKeyboardButton(
                        "اوامر الادمن", callback_data="adm"), 
                ],[
                
                    InlineKeyboardButton(
                        "★⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝⚡", url=f"https://t.me/UC_IU"),
                ],

            ]

        ),

    )
