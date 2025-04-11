#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>‣ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>ʜᴩ_ʀᴀᴊ</a>\n‣ Language : <code>Python3</code>\n‣ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\‣ ʙᴏᴛ sᴇʀᴠᴇʀ  : <a href='https://t.me/Filmy_Fusion'>ʜᴇʀᴏᴋᴜ</a>\n○ Channel : @Filmy_Fusion \n‣ ᴄʟᴏɴ ʙᴏᴛ : <a href='https://t.me/HP_AutoFilterBot'>ᴍᴀᴀᴛᴇʀ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
