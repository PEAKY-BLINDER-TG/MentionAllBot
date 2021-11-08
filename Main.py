import os
from pyrogram import Client

APP_ID = "3637235"
API_HASH = "028885dcbc64a4b56c47bdad0367523b"
TG_BOT_TOKEN = "2110416751:AAF20hCuQlVsIIGEmJCSd03Z8H4rFbrm_6g"

plugins = dict(
    root="plugins"
)

Bot = Client(
    "chumma oru bot",
    api_id=APP_ID,
   api_hash=API_HASH,
   bot_token=TG_BOT_TOKEN,
   plugins=plugins
)

Bot.run()
