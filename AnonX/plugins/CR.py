import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

                
@app.on_message(
    command(["مطورين سي ار","المطورين","مطورين","مطورين dark"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6ccfb45597628a287bbc8.jpg",
        caption=f"""⩹━⊷⌯⌞َِ𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝⌯⊶━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين مـرعـب ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝━⊶━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "مـ ـرعـ ـب قـ ـلَبـ ـوٌ لَنـ ـفـ ـسـ ـوٌوٌ 🕷>", url=f"https://t.me/M0R_3b1"), 
                 ],[
                    InlineKeyboardButton(
                        "ألموع ـلم مـ ــيــ ــدؤ ســ ـــنــ ــدأل >3`", url=f"https://t.me/EU_ET"),
                ],[
                    InlineKeyboardButton(
                       "𝘽 𝙀 𝘽 𝙊 🇵🇸 [ بـتـاع طـنطـا ]", url=f"https://t.me/V_I_P3"),
                    InlineKeyboardButton(
                        "قناه السورس", url=f"https://t.me/UC_IU"),
                ],[
                
                    InlineKeyboardButton(
                        "⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝", url=f"https://t.me/UC_IU"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["المطور"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("M0R_3b1")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━⊷━⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝━⊶━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━⊷━⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝━⊶━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["مرعب"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("M0R_3b1")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━⊷━⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝━⊶━⩺\n\n¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━⊷━⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝━⊶━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["ميدو"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("EU_ET")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝━⊶━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━⊷━⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝━⊶━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    

@app.on_message(
    command(["بيبو"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("V_I_P3")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━⊷━⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝━⊶━⩺\n\n ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━⊷━⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝━⊶━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    


@app.on_message(
    command(["/api"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c5952790fa8235f499749.jpg",
        caption=f"""⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝*\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس مـرعب\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**⩹━━⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙈َِ𝙊َِ𝙍3َِ𝘽", url=f"https://t.me/M0R_3b1"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝⚡", url=f"https://t.me/UC_IU"),
                ],

            ]

        ),

    )



@app.on_message(
    command(["هقراااااااتتاتتبنيتيخيريت"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c5952790fa8235f499749.jpg",
        caption=f"""**⩹⊷━⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم تشغيل القرأن الخاص بسورس مـرعب⩹━★⊷⌯⌞\nلتتمكن من استخدام اوامر القرأن اكتب \n سورة + اسم السورة بالاسفل👇\n**⩹━━⌞  𝚂𝙾𝚄𝚁𝙲𝙴 𝙳𝙰𝚁𝙺 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝙳𝙰𝚁𝙺", url=f"https://t.me/T4_Mohamed"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞  𝚂𝙾𝚄𝚁𝙲𝙴 𝙳𝙰𝚁𝙺 ⌝⚡", url=f"https://t.me/T4_Mohamed"),
                ],

            ]

        ),

    )



    
