import asyncio
import random
from AnonX.misc import SUDOERS
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup)
from pyrogram import filters, Client
from AnonX import app
from config import *

bot_name = {}
botname = {}

name = "مارش"

@app.on_message(filters.regex("تعيين اسم البوت")& filters.private & SUDOERS, group=7113)
async def set_bot_name(client, message):
    global name
    ask = await app.ask(message.chat.id, "ارسل الاسم الجديد", timeout=300)
    name = ask.text
    await message.reply_text("تم تعيين الاسم بنجاح")

caesar_responses = [
    "اسمي {name} يصحبي",
    "يسطا قولتلك اسمي {name} الاه",
    "نعم يحب",
    "قول يقلبو",
    "يسطا هوا عشان بحبك تصعدني؟",
    "يعم والله بحبك بس ناديلي ب {name}",
    "تعرف بالله هحبك أكتر لو ناديتلي {name}",
    "اي ي معلم مين مزعلك",
    "متصلي على النبي كدا",
    "مش فاضيلك نصايح وكلمني",
    "يسطا قولي مين مزعلك وعايزك تقعد وتتفرج على أخوك",
    "انجز عايزني أشقطلك مين؟",
    "شكلها منكدا عليك وجاي تطلعهم علينا",
    "ورحمة أبويا اسمي {name}",
]

@app.on_message(filters.command(["بوت", "البوت"], ""), group=71135)
async def caesar_bot(client, message):
    global name
    bot_username = (await app.get_me()).username
    bar = random.choice(caesar_responses).format(name=name)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("خدني لجروبك والنبي🥺♥", url=f"https://t.me/{bot_username}?startgroup=True")]
    ])

    await message.reply_text(
        text=f"**[{bar}](https://t.me/{bot_username}?startgroup=True)**",
        disable_web_page_preview=True,
        reply_markup=keyboard
    )
    txt = [
" هآي تع اشب شااي • 😹💔"
        ]
@app.on_message(filters.command(["هاي"], ""), group=73)

async def caesar(client: Client, message: Message):

      a = random.choice(txt)

      await message.reply(

        f"{a}")
        
        
thxt = [
" وعليكم السلام 🌝💜"
        ]
@app.on_message(filters.command(["السلام عليكم"], ""), group=173)

async def caesar(client: Client, message: Message):

      a = random.choice(thxt)

      await message.reply(

        f"{a}")        
     
htxt = [
" خدوني معاكم برايفت والنبي 🥺💔"
        ]

@app.on_message(filters.command(["برايفت"], ""), group=273)

async def caesar(client: Client, message: Message):

      a = random.choice(htxt)

      await message.reply(

        f"{a}")   
        
htt = [
" نزل عينك تحت كدا علشان هتخاد علي قفاك 😒❤️"
        ]

@app.on_message(filters.command(["🙄"], ""), group=373)

async def caesar(client: Client, message: Message):

      a = random.choice(htt)

      await message.reply(

        f"{a}")           
        
htx = [
" مع الف سلامه يقلبي متجيش تاني 😹💔🎶"
        ]

@app.on_message(filters.command(["سلام"], ""), group=253)

async def caesar(client: Client, message: Message):

      a = random.choice(htx)

      await message.reply(

        f"{a}")        

ht = [
" عليه الصلاه والسلام 🌝💛"
        ]

@app.on_message(filters.command(["صلي علي النبي"], ""), group=673)

async def caesar(client: Client, message: Message):

      a = random.choice(ht)

      await message.reply(

        f"{a}")

hxt = [
" نعم الله عليك 🌚❤️"
        ]

@app.on_message(filters.command(["نعم"], ""), group=2073)

async def caesar(client: Client, message: Message):

      a = random.choice(txt)

      await message.reply(

        f"{a}")

hytxt = [
" القمر ده شبهك 🙂❤️"
        ]

@app.on_message(filters.command(["🌚"], ""), group=2173)

async def caesar(client: Client, message: Message):

      a = random.choice(hytxt)

      await message.reply(

        f"{a}")   

hgtxt = [
" بتفكر في اي 🤔"
        ]

@app.on_message(filters.command(["🤔"], ""), group=2573)

async def caesar(client: Client, message: Message):

      a = random.choice(hgtxt)

      await message.reply(

        f"{a}")   

ghtxt = [
" ضحكتك عثل زيكك ينوحيي 🌝❤️"
        ]

@app.on_message(filters.command(["😂"], ""), group=26773)

async def caesar(client: Client, message: Message):

      a = random.choice(ghtxt)

      await message.reply(

        f"{a}")   

jhtxt = [
" متزعلش بحبك 😻🤍"
        ]

@app.on_message(filters.command(["🥺"], ""), group=26473)

async def caesar(client: Client, message: Message):

      a = random.choice(jhtxt)

      await message.reply(

        f"{a}")   

ahtxt = [
" بتعيط تيب لي طيب 😥"
        ]

@app.on_message(filters.command(["😭"], ""), group=23573)

async def caesar(client: Client, message: Message):

      a = random.choice(ahtxt)

      await message.reply(

        f"{a}")   

shtxt = [
" نا عايز مح انا كمان 🥺💔"
        ]

@app.on_message(filters.command(["💋"], ""), group=29773)

async def caesar(client: Client, message: Message):

      a = random.choice(shtxt)

      await message.reply(

        f"{a}")   

dhtxt = [
" عدل وشك ونت بتكلمني 😒🙄"
        ]

@app.on_message(filters.command(["😒"], ""), group=2873)

async def caesar(client: Client, message: Message):

      a = random.choice(dhtxt)

      await message.reply(

        f"{a}")
mhtxt = [
"محات حياتي يروحي 🌝❤️"
        ]

@app.on_message(filters.command(["محح"], ""), group=2601473)

async def caesar(client: Client, message: Message):

      a = random.choice(mhtxt)

      await message.reply(

        f"{a}")   

lhtxt = [
" وانا كمان بعشقك يا روحي 🤗🥰"
        ]

@app.on_message(filters.command(["بحبك"], ""), group=231673)

async def caesar(client: Client, message: Message):

      a = random.choice(lhtxt)

      await message.reply(

        f"{a}")   

xhtxt = [
" دايما ياحبيبي 🌝❤️"
        ]

@app.on_message(filters.command(["الحمدلله"], ""), group=274683)

async def caesar(client: Client, message: Message):

      a = random.choice(xhtxt)

      await message.reply(

        f"{a}")   

dfhtxt = [
" بنهش كتاكيت احنا هنا ولا اي ??😹"
        ]

@app.on_message(filters.command(["هشش"], ""), group=2756033)

async def caesar(client: Client, message: Message):

      a = random.choice(dfhtxt)

      await message.reply(

        f"{a}")   

nhtxt = [
" هلا بيك ياروحي 👋"
        ]

@app.on_message(filters.command(["هلا"], ""), group=207973)

async def caesar(client: Client, message: Message):

      a = random.choice(nhtxt)

      await message.reply(

        f"{a}")   

phtxt = [
" وحيات امك ياكبتن خدوني معاكو بيف 🥺💔"
        ]

@app.on_message(filters.command(["بف"], ""), group=270973)

async def caesar(client: Client, message: Message):

      a = random.choice(phtxt)

      await message.reply(

        f"{a}")   

ihtxt = [
" ونجيب اشخاص 😂👻"
        ]

@app.on_message(filters.command(["خاص"], ""), group=273573)

async def caesar(client: Client, message: Message):

      a = random.choice(ihtxt)

      await message.reply(

        f"{a}")   

uhtxt = [
" انت الخير يعمري 🌝❤️"
        ]

@app.on_message(filters.command(["بخير"], ""), group=279373)

async def caesar(client: Client, message: Message):

      a = random.choice(uhtxt)

      await message.reply(

        f"{a}")   

rhtxt = [
" اه اي يا قدع عيب 😹💔"
        ]

@app.on_message(filters.command(["اه"], ""), group=267473)

async def caesar(client: Client, message: Message):

      a = random.choice(rhtxt)

      await message.reply(

        f"{a}")   

htxtk = [
"خخخ امال 😹"
        ]

@app.on_message(filters.command(["حصل"], ""), group=225973)

async def caesar(client: Client, message: Message):

      a = random.choice(htxtk)

      await message.reply(

        f"{a}")

asdhtxt = [
" لا عيب بتكسف 😹💔"
        ]

@app.on_message(filters.command(["تع"], ""), group=200873)

async def caesar(client: Client, message: Message):

      a = random.choice(asdhtxt)

      await message.reply(

        f"{a}")   

pokghtxt = [
" ده نورك ي قلبي 🌝💙"
        ]

@app.on_message(filters.command(["منور"], ""), group=200173)

async def caesar(client: Client, message: Message):

      a = random.choice(pokghtxt)

      await message.reply(

        f"{a}")   

ijkhtxt = [
" اي الثقافه دي 😒😹"
        ]

@app.on_message(filters.command(["ويت"], ""), group=200273)

async def caesar(client: Client, message: Message):

      a = random.choice(ijkhtxt)

      await message.reply(

        f"{a}")   

kghtxt = [
"ع فين لوين رايح وسايبنى 🥺💔"
        ]

@app.on_message(filters.command(["باي"], ""), group=200373)

async def caesar(client: Client, message: Message):

      a = random.choice(kghtxt)

      await message.reply(

        f"{a}")   

lphtxt = [
" اهدا يوحش ميصحش كدا 😒??"
        ]

@app.on_message(filters.command(["خخخ"], ""), group=200473)

async def caesar(client: Client, message: Message):

      a = random.choice(lphtxt)

      await message.reply(

        f"{a}")   

tthtxt = [
" العفو ياروحي 🙈🌝"
        ]

@app.on_message(filters.command(["شكرا"], ""), group=200573)

async def caesar(client: Client, message: Message):

      a = random.choice(tthtxt)

      await message.reply(

        f"{a}")   

qqhtxt = [
" انت الي حلو ياقمر 🤤🌝"
        ]

@app.on_message(filters.command(["حلوه"], ""), group=200673)

async def caesar(client: Client, message: Message):

      a = random.choice(qqhtxt)

      await message.reply(

        f"{a}")   

wwhtxt = [
" موت بعيد م ناقصين مصايب 😑😂"
        ]

@app.on_message(filters.command(["بموت"], ""), group=200773)

async def caesar(client: Client, message: Message):

      a = random.choice(wwhtxt)

      await message.reply(

        f"{a}")   

zzhtxt = [
"فرح خالتك قريب 😹💋💃🏻"
        ]

@app.on_message(filters.command(["تيب"], ""), group=200873)

async def caesar(client: Client, message: Message):

      a = random.choice(zzhtxt)

      await message.reply(

        f"{a}")   

vvhtxt = [
" جتك اوهه م سامع ولا ايي 😹👻"
        ]

@app.on_message(filters.command(["اي"], ""), group=200973)

async def caesar(client: Client, message: Message):

      a = random.choice(vvhtxt)

      await message.reply(

        f"{a}")   

xxhtxt = [
" حضرلك الخير يارب 🙂❤️"
        ]

@app.on_message(filters.command(["حاضر"], ""), group=2000173)

async def caesar(client: Client, message: Message):

      a = random.choice(xxhtxt)

      await message.reply(

        f"{a}")   

cchtxt = [
" لف ورجع تانى مشحوار 😂🚶‍♂👻"
        ]

@app.on_message(filters.command(["جيت"], ""), group=2000273)

async def caesar(client: Client, message: Message):

      a = random.choice(cchtxt)

      await message.reply(

        f"{a}")   

kjjhtxt = [
"يوه خضتني ياسمك اي 🥺💔"
        ]

@app.on_message(filters.command(["بخ"], ""), group=2000373)

async def caesar(client: Client, message: Message):

      a = random.choice(kjjhtxt)

      await message.reply(

        f"{a}")   

ffhtxt = [
" خلصتت روحكك يبعيد 😹💔"
        ]

@app.on_message(filters.command(["خلاص"], ""), group=2000473)

async def caesar(client: Client, message: Message):

      a = random.choice(ffhtxt)

      await message.reply(

        f"{a}")   

pphtxt = [
" امك اسمها احلام 😹😹"
        ]

@app.on_message(filters.command(["تمام"], ""), group=2000573)

async def caesar(client: Client, message: Message):

      a = random.choice(pphtxt)

      await message.reply(

        f"{a}")   

oohtxt = [
" اوه ياه 🌝😂"
        ]

@app.on_message(filters.command(["حبيبي"], ""), group=20703)

async def caesar(client: Client, message: Message):

      a = random.choice(oohtxt)

      await message.reply(

        f"{a}")   

llhtxt = [
" كفيه شقط سيب حاجه لغيرك 😎😂"
        ]

@app.on_message(filters.command(["سيفي"], ""), group=20713)

async def caesar(client: Client, message: Message):

      a = random.choice(llhtxt)
      
      await message.reply(

        f"{a}")   

kkhtxt = [
"كفيه شقط سيب حاجه لغيرك 😎😂"
        ]

@app.on_message(filters.command(["سي في"], ""), group=22703)

async def caesar(client: Client, message: Message):

      a = random.choice(kkhtxt)

      await message.reply(

        f"{a}")   
 #كود ردود بسيط للسورس الميوزك بنسخه انوكس 
#مقدم من قيصر   @c_a_s_e_r_h
#مقدم من القيصر صاحب العظمه @c_a_s_e_r_h                
#قناه سورس القيصر صاحب العظمه  @COURSE_CAESAR
