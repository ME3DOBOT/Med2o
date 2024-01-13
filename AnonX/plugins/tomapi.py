import asyncio
import os
from pyrogram.types import CallbackQuery
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified



@app.on_message(
    filters.command("tnt")
    
)
async def cr_source(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/74d7222ff0fdc7c24a938.jpg",
        caption=f"""**⩹━⊷━⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝━⊶━⩺**\nمرحبا بك عزيزي {message.from_user.mention}\nانا بوت الذكاء الاصطناعي الخاص بسورس cr \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n**⩹━⊷━⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝━⊶━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "طريقة الإستخدام", callback_data="usage"), 
                 ],[
                    InlineKeyboardButton(
                        "𝙈َِ𝙊َِ𝙍3َِ𝘽", url=f"https://t.me/M0R_3b1"),
                    InlineKeyboardButton(
                        "ᴍᴇᴅᴏ", url=f"https://t.me/EU_ET"),
                ],[
                
                    InlineKeyboardButton(
                        "★⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝⚡", url=f"https://t.me/UC_IU"),
                ],

            ]

        ),

    )

    
@app.on_callback_query(filters.regex("usage"))
async def cr_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**⩹━⊷⌯⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝⌯⊶━⩺**
★¦ اهلا بك عزيزي في قسم الأوامر
★¦ لتتمكن من تشغيل الذكاء الاصطناعي فقط اكتب
★¦ /gpt - لـلـسـؤال آي سـؤال بالـذكـاء الاسـطـناعي

**⩹━⊷⌯⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝⌯⊶━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "العودة", callback_data="back"), 
                ]
            ]
        )
    )

    
@app.on_callback_query(filters.regex("back"))
async def cr_back(_, callback_query: CallbackQuery):
    message = callback_query.message
  
    await message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("طريقة الإستخدام", callback_data="tommm")],
            [InlineKeyboardButton("𝙈َِ𝙊َِ𝙍3َِ𝘽", url=f"https://t.me/M0R_3b1"),
             InlineKeyboardButton("ᴍᴇᴅᴏ", url=f"https://t.me/EU_ET")],
            [InlineKeyboardButton("★⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝⚡", url=f"https://t.me/UC_IU")],
        ]
    ))

