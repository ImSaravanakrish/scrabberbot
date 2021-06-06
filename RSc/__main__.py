from telethon import events
from RSc import TOKEN, tbot
from telethon.tl.functions.users import GetFullUserRequest
import RSc.events

CHANNEL_ID = -1001379422786

client = TelegramClient(StringSession(string_session), api_id, api_hash)
client.start()

try:
    tbot.start(bot_token=TOKEN)
except Exception:
    print("Bot Token Invalid")
    exit(1)

async def start_log():
    await client.send_message(
        CHANNEL_ID, "**Scrapper Started!**"
    )


tbot.loop.run_until_complete(start_log())

tbot.run_until_disconnected()

