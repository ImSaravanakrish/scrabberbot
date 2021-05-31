from telethon import TelegramClient
from telethon.sessions import StringSession
import os, sys
import logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
LOGGER = logging.getLogger(__name__)

S_1 = os.environ.get("STRING_1")
S_2 = os.environ.get("STRING_2")
S_3 = os.environ.get("STRING_3")
S_4 = os.environ.get("STRING_4")
S_5 = os.environ.get("STRING_5")

K_1 = os.environ.get("KEY_1")
K_2 = os.environ.get("KEY_2")
K_3 = os.environ.get("KEY_3")
K_4 = os.environ.get("KEY_4")
K_5 = os.environ.get("KEY_5")

H_1 = os.environ.get("HASH_1")
H_2 = os.environ.get("HASH_2")
H_3 = os.environ.get("HASH_3")
H_4 = os.environ.get("HASH_4")
H_5 = os.environ.get("HASH_5")

APP_ID = os.environ.get("APP_ID")
HASH_API = os.environ.get("HASH_API")

OWNER_ID = os.environ.get("OWNER_ID")

TOKEN = os.environ.get("TOKEN")
tbot = TelegramClient(None, APP_ID, HASH_API)

# ubot = TelegramClient(StringSession(S_1), APP_ID, HASH_API)
vbot = TelegramClient(StringSession(S_2), APP_ID, HASH_API)
# wbot = TelegramClient(StringSession(S_3), APP_ID, HASH_API)
# xbot = TelegramClient(StringSession(S_4), APP_ID, HASH_API)
# ybot = TelegramClient(StringSession(S_5), APP_ID, HASH_API)


try:
  # ubot.start()
  vbot.start()
  # wbot.start()
  # xbot.start()
  # ybot.start()
except Exception as e:
  print(e)
  sys.exit()

