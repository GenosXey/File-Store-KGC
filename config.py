0# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport
#
# Copyright (C) 2025 by Codeflix-Bots@Github, < https://github.com/Codeflix-Bots >.
#
# This file is part of < https://github.com/Codeflix-Bots/FileStore > project,
# and is released under the MIT License.
# Please see < https://github.com/Codeflix-Bots/FileStore/blob/master/LICENSE >
#
# All rights reserved.
#


import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7995818026:AAEUEb_0R1G9N2If4jJyAU-BI4wx4a3S0yk")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "24817837"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "acd9f0cc6beb08ce59383cf250052686")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002265513823"))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "Sankare87")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1682759613"))
#Port
PORT = os.environ.get("PORT", "8080")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Ethan:Ethan123@telegrambots.lva9j.mongodb.net/?retryWrites=true&w=majority&appName=TELEGRAMBOTS")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#Time in seconds for message delete, put 0 to never delete
TIME = int(os.environ.get("TIME", "0"))


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "0"))
#put 0 to disable
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002406858001"))#put 0 to disable
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1002278232343"))#put 0 to disable
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "0"))#put 0 to disable

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://iili.io/37b39B1.md.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://iili.io/3uLhgVf.md.jpg")

# Turn this feature on or off using True or False put value inside  ""
# TRUE for yes FALSE if no 
TOKEN = True if os.environ.get('TOKEN', "False") == "True" else False 
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "publicearn.online")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "adabe1c0675be8ffc5ccbc84a9a65bc5a5d3ec69")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 600)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "False")
TUT_VID = os.environ.get("TUT_VID","https://t.me/hwdownload/3")


HELP_TXT = "<b>Toi aussi tu veux un bot pareil que moi ??\n\nContact juste mon créateur : @Kingcey</b>"

ABOUT_TXT = "<b><blockquote>◈ Propio: <a href=https://t.me/Sankare87>سنكاري عبد الرشيد</a>\n◈ AUTH: <a href=https://t.me/BotZFlix>ᴏᴛᴀᴋᴜғʟɪx</a>\n◈ Canal Anime: <a href=https://t.me/Otaku_Haven_hebdo>Otaku Haven</a>\n◈ Propio : <a href=https://t.me/Sankare87>سنكاري عبد الرشيد</a></blockquote></b>"


START_MSG = os.environ.get("START_MESSAGE", "<b>Yo {first}\n\n 𝚃'𝚊𝚍𝚘𝚛𝚎 𝚕𝚎𝚜 𝚊𝚗𝚒𝚖𝚎𝚜 ? ! 𝙹𝚎 𝚜𝚞𝚒𝚜 𝚕à 𝚙𝚘𝚞𝚛 𝚝'𝚊𝚒𝚍𝚎𝚛 à 𝚝𝚛𝚘𝚞𝚟𝚎𝚛 𝚌𝚎 𝚚𝚞𝚎 𝚝𝚞 𝚌𝚑𝚎𝚛𝚌𝚑𝚎𝚜.\n\n𝚅é𝚛𝚒𝚏𝚒𝚎 𝚖𝚊 𝚌𝚑𝚊î𝚗𝚎 𝚌𝚒-𝚍𝚎𝚜𝚜𝚘𝚞𝚜 𝚙𝚘𝚞𝚛 𝚎𝚗 𝚜𝚊𝚟𝚘𝚒𝚛 𝚙𝚕𝚞𝚜 !👇\n\n Propulseé Par <a href=https://t.me/Tokyo_Streame>Tokyo Stream</b>")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "1682759613 7428552084 7831789273 5231212075 7328629001").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Genjutsu {first}\n\n<b>Pour recevoir le fichier de l'animé, Tu dois d'abord rejoindre mon canal puis cliquer sur récupérer</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• {filename}</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! 𝚃𝚞 𝚗'𝚎𝚜 𝚙𝚊𝚜 𝚖𝚘𝚗 ꜱᴇɴᴘᴀɪ!!"

ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
