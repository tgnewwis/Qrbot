import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram import Client, filters,emoji
from pyrogram.types import Message
import pyqrcode
import png

HB = Client(
    "YOUTUBE Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)  

START_TEXT = """
I am a QR Code Bot 🤖**

>> `I can generate links to QR Code with QR Code decode to links support. 🚀`

Made by @wisula4 🇱🇰"""

HELP_TEXT = """**Hey, Follow these steps:**

➠ Send me a link I will generate the QR code of that link 🤭
➠ Send me a QR code image I will decode that image and convert to link 👌
➠ Made in sri lanka 🇱🇰
"""

ABOUT_TEXT = """
 🤖<b>BOT :QR CODE GENERATOR </b>
 
 🧑🏼‍💻<b>DEV : </b>  <a href='https://t.me/wisula4'>wisula</a>
 
 📢<b>CHANNEL :</b> </b>  <a href='https://t.me/EpicBotsSl'>Epic bots</a>
 
 📝<b>Language :</b>  <a href='https://python.org/'>Python3</a>
 
 🧰<b>Frame Work :</b>  <a href='https://pyrogram.org/'>Pyrogram</a>
 
 🤩<b>SOURCE :</b>  <a href='https://t.me/MW_GIVEAWAYS'>MW GIVEAWAYS</a>
 
 
"""
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://t.me/EpicBotsSl'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://t.me/wisula4')
        ],[
        InlineKeyboardButton('🆘HELP🆘', callback_data='help'),
        InlineKeyboardButton('🤗ABOUT🤗', callback_data='about'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )


result_buttons = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://t.me/EpicBotsSl'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://t.me/wisula4')
        ],[
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://t.me/EpicBotsSl'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://t.me/wisula4')
        ],[
        InlineKeyboardButton('🏡HOME🏡', callback_data='home'),
        InlineKeyboardButton('🤗ABOUT🤗', callback_data='about'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://t.me/EpicBotsSl'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://t.me/wisula4')
        ],[
        InlineKeyboardButton('🏡HOME🏡', callback_data='home'),
        InlineKeyboardButton('🆘HELP🆘', callback_data='help'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )

SOURCE_TEXT = """</b>PRESS SOURCE BUTTON \n FOR SOURCE CODE</b>"""
SOURCE_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('✅SOURCE✅', url='https://t.me/wisula4'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://t.me/wisula4')
        ],[
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )

result_buttons = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://t.me/EpicBotsSl'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://t.me/wisula4')
        ],[
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )

result_buttons2 = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton('✅GENERATE✅ ' , callback_data='generate')
    ],[
        InlineKeyboardButton('❌CANCEL❌', callback_data='close')
    ]]
   )
result_text = """**JOIN @EpicBotsSl**"""


@HB.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@HB.on_message(filters.command(["help"]))
async def help_message(bot, update):
    text = HELP_TEXT
    reply_markup = HELP_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@HB.on_message(filters.command(["about"]))
async def about_message(bot, update):
    text = ABOUT_TEXT
    reply_markup = ABOUT_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )
@HB.on_message(filters.command(["source"]))
async def about_message(bot, update):
    text = SOURCE_TEXT
    reply_markup = SOURCE_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )
@HB.on_message()
async def main(client:Client, message:Message):
    global url
    global var
    var = message.text
    url = message.text
    photo=pyqrcode.create(url)
    photo.png('HB.png',scale=20)
    await message.reply_text(
        text="**CHOOSE ANY OPTION 👇🏻**",
        reply_markup=result_buttons2,
        quote=True,
    )

@HB.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    elif update.data == "generate":
        await  HB.send_photo(
        chat_id = update.message.chat.id,
        photo='HB.png',
        caption=result_text,
        reply_markup=result_buttons
        )  
        await update.message.delete()
    else:
        await update.message.delete()
print("HB")
HB.run()
