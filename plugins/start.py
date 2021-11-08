import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import logging
from pyrogram import Client as bot
from pyrogram import filters

@bot.on_message(filters.command(["info"]) & filters.private, group=1)
async def start(bot, update):
    await update.reply_photo(
        photo="https://telegra.ph/file/860cc0afcf63e109bda07.jpg",
        caption=f"""<b>Hᴇʏ {update.from_user.mention}
ഞാൻ <a href="https://t.me/cinemazilla">Cɪɴᴇᴍᴀ Zɪʟʟᴀ</a> എന്ന ഗ്രൂപ്പിൽ  ചുമ്മാ ഇരികുനാ bot അണ്
നോക്കണ്ടാ എന്നെ മറ്റു ഗ്രൂപ്പിൽ ഒന്നും ഉപയോഗിക്കാൻ കഴിയുകയില്ല!
𝙼𝙰𝙸𝙽𝚃𝙰𝙸𝙽𝙴𝙳 𝙱𝚈 <a href="https://t.me/Peaky_blinder_tg">𝚃𝙷𝙸𝚂 𝙱𝙾𝚈𝚈</a></b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("➕ Add Me To Your Group ➕", url="t.me/Lissa_test_bot?startgroup=true"),
                ],[
                    InlineKeyboardButton("🕵‍♂ Creator", callback_data="devs"),
                    InlineKeyboardButton("⚠️ Group", url="https://t.me/peaky_blinder_tg"),
                ],[
                    InlineKeyboardButton("💡 Help", callback_data="home"),
                    InlineKeyboardButton("😃 About", callback_data="about"),
                ]
            ]
        ),
    )

