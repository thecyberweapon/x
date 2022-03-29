#ChauhanMahesh/Vasusen/WorkerBots/COL

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("2164808")
API_HASH = config("2af46b76e38461db8b0b078dfa79c2a8")
BOT_TOKEN = config("5225492558:AAHj4dyBm4BR5D_0LnDkEpzAxIcZTs2W7Nw")
SESSION = config("BQB7B_v9wssEiTR9GxPr-1WHd9y1j5Ph1yDXGSNrpdQHrvofEGbsghSpbFWjXJWfLjs3rhfRe-WnhmfrG-wEexgW-nGwls7Beuf3dt1B1Kz1MzUQ9OJd57DBCt3hWzrq7m_YTsfTwMQ_cEAZswR4EDNJLTGIa8yjjCXm_WjMhjiEd4rzh5TB3diToxhleF_8xP41_LLTkfMygBk5gcldbKTc_cYhFhIsOC7fAm8Ye00brWP3xQsxMM_mLcrNxztROqJlznBW093gnzBgF88HuYvQg0mZXJmbRMVJgVKPcNIeG54RRQyxc0Jm2Zzz6LKsnnNPmH41wJb9yAYSca3d_FnLAAAAATr0kc8A")
FORCESUB = config("toxiclectuers")
AUTH = config("5284073935")

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
