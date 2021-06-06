from telethon import events
from RSc import TOKEN, tbot
import RSc.events

CHANNEL_ID = -1001379422786
try:
    tbot.start(bot_token=TOKEN)
except Exception:
    print("Bot Token Invalid")
    exit(1)

async def start_log(event):
    await tbot.send_message(
        event.chat_id, "**Scrapper Started!**"
    )


tbot.loop.run_until_complete(start_log(event))

tbot.run_until_disconnected()

