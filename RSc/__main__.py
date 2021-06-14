from sys import argv, exit
from telethon import events
from RSc import TOKEN, tbot
from telethon.sync import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest
import RSc.events

try:
    tbot.start(bot_token=TOKEN)
except Exception:
    print("Network Error !")
    exit(1)

if len(argv) not in (1, 3, 4):
    tbot.disconnect()
else:
    tbot.run_until_disconnected()
