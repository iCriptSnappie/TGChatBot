

import asyncio
import random

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message


from nexichat import nexichat
from nexichat.database.chats import add_served_chat
from nexichat.database.users import add_served_user
from nexichat.modules.helpers import (
    CLOSE_BTN,
    DEV_OP,
    HELP_BTN,
    HELP_BUTN,
    HELP_READ,
    HELP_START,
    SOURCE_READ,
    START,
)

from config import IMG, STICKER, EMOJIOS, SOURCE_MDEIA, POST_URL, MSG_POST_URL, PROMO



@nexichat.on_cmd(["start", "aistart"])
async def start(_, m: Message):
    try:
        if m.chat.type == ChatType.PRIVATE:
            accha = await m.reply_text(text=random.choice(EMOJIOS))
            await asyncio.sleep(1.3)
            await accha.edit("**ʀᴀᴅʜᴇ ʀᴀᴅʜᴇ🙏🏻❤**")
            await asyncio.sleep(1)
            await accha.edit("**ᴊᴀɪ sʜʀᴇᴇ ᴋʀɪsʜɴ🙏🏻❤**")
            await asyncio.sleep(1)
            await accha.delete()
            umm = await m.reply_sticker(sticker=random.choice(STICKER))
            await asyncio.sleep(2)
            await umm.delete()
            await m.reply_photo(
                photo=random.choice(IMG),
                caption=f"""**๏ ʜᴇʏ, ɪ ᴀᴍ {nexichat.name}**\n**➻ ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛʙᴏᴛ.**\n**──────────────**\n**➻ ᴜsᴀɢᴇ /chatbot [ᴏɴ/ᴏғғ]**\n<b>๏ ʜɪᴛ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ғᴏʀ ʜᴇʟᴘ</b>""",
                reply_markup=InlineKeyboardMarkup(DEV_OP),
            )
            await asyncio.sleep(2)
            await m.reply_text(
                text=PROMO,
                disable_web_page_preview=True
            )
            await asyncio.sleep(2)
            await m.reply_text(
                text=random.choice(POST_URL)
            )
            await add_served_user(m.from_user.id)
        else:
            await m.reply_photo(
                photo=random.choice(IMG),
                caption=START,
                reply_markup=InlineKeyboardMarkup(HELP_START),
            )
            await add_served_chat(m.chat.id)
    except Exception as e:
        print(f"Error in start_command: {e}")
        # Add additional error handling if needed

@nexichat.on_cmd("help")
async def help(client: nexichat, m: Message):
    try:
        if m.chat.type == ChatType.PRIVATE:
            hmm = await m.reply_photo(
                photo=random.choice(IMG),
                caption=HELP_READ,
                reply_markup=InlineKeyboardMarkup(HELP_BTN),
            )
            await add_served_user(m.from_user.id)
        else:
            await m.reply_photo(
                photo=random.choice(IMG),
                caption="**ʜᴇʏ, ᴘᴍ ᴍᴇ ғᴏʀ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs!**",
                reply_markup=InlineKeyboardMarkup(HELP_BUTN),
            )
            await add_served_chat(m.chat.id)
    except Exception as e:
        print(f"Error in help_command: {e}")


@nexichat.on_cmd("repo")
async def repo_command(_, m: Message):
    try:
        # Assuming `send_video` is provided by `nexichat` or a related library
        await nexichat.send_video(
            m.chat_id,
            SOURCE_MEDIA,
            has_spoiler=True
        )
        await asyncio.sleep(2)  # Optional delay after sending the video
        
        # Assuming POST_URL is a list of URLs and random.choice selects one
        await m.reply_text(
            text=random.choice(POST_URL)
        )
    except Exception as e:
        print(f"Error in repo_command: {e}")


@nexichat.on_message(filters.new_chat_members)
async def welcome(_, m: Message):
    for member in m.new_chat_members:
        await m.reply_photo(photo=random.choice(IMG), caption=START)
