# Copyright (c) 2025 Nand Yaduwanshi <NoxxOP>
# Location: Supaul, Bihar
#
# All rights reserved.
#
# This code is the intellectual property of Nand Yaduwanshi.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: badboy809075@gmail.com

import random
import requests
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from nekosbest import Client as NekoClient

from HELLBOTS import app
from config import SUPPORT_CHAT

BUTTON = InlineKeyboardMarkup([[InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url=SUPPORT_CHAT)]])

MEDIA = {
    "cutie": "https://graph.org/file/24375c6e54609c0e4621c.mp4",
    "horny": "https://graph.org/file/eaa834a1cbfad29bd1fe4.mp4",
    "hot": "https://graph.org/file/745ba3ff07c1270958588.mp4",
    "sexy": "https://graph.org/file/58da22eb737af2f8963e6.mp4",
    "gay": "https://graph.org/file/850290f1f974c5421ce54.mp4",
    "lesbian": "https://graph.org/file/ff258085cf31f5385db8a.mp4",
    "boob": "https://i.gifer.com/8ZUg.gif",
    "cock": "https://telegra.ph/file/423414459345bf18310f5.gif",
}

TEMPLATES = {
    "cutie": "🍑 {mention} ɪꜱ {percent}% ᴄᴜᴛᴇ ʙᴀʙʏ🥀",
    "horny": "🔥 {mention} ɪꜱ {percent}% ʜᴏʀɴʏ!",
    "hot": "🔥 {mention} ɪꜱ {percent}% ʜᴏᴛ!",
    "sexy": "💋 {mention} ɪꜱ {percent}% ꜱᴇxʏ!",
    "gay": "🍷 {mention} ɪꜱ {percent}% ɢᴀʏ!",
    "lesbian": "💜 {mention} ɪꜱ {percent}% ʟᴇꜱʙɪᴀɴ!",
    "boob": "🍒 {mention}ꜱ ʙᴏᴏʙ ꜱɪᴢᴇ ɪꜱ {percent}!",
    "cock": "🍆 {mention} ᴄᴏᴄᴋ ꜱɪᴢᴇ ɪꜱ {percent}ᴄᴍ!",
}
def get_user_mention(message: Message) -> str:
    user = message.reply_to_message.from_user if message.reply_to_message else message.from_user
    return f"[{user.first_name}](tg://user?id={user.id})"


def get_reply_id(message: Message) -> int | None:
    return message.reply_to_message.message_id if message.reply_to_message else None


async def handle_percentage_command(_, message: Message):
    command = message.command[0].lower()
    if command not in MEDIA or command not in TEMPLATES:
        return

    mention = get_user_mention(message)
    percent = random.randint(1, 100)
    text = TEMPLATES[command].format(mention=mention, percent=percent)
    media_url = MEDIA[command]

    await app.send_document(
        message.chat.id,
        media_url,
        caption=text,
        reply_markup=BUTTON,
        reply_to_message_id=get_reply_id(message),
    )


for cmd in ["cutie", "horny", "hot", "sexy", "gay", "lesbian", "boob", "cock"]:
    app.on_message(filters.command(cmd))(handle_percentage_command)

#---------------------------------------------punch animantiation vala-----------------
neko_client = NekoClient()

commands = {
    "punch": {"emoji": "💥", "text": "punched"},
    "slap": {"emoji": "😒", "text": "slapped"},
    "hug": {"emoji": "🤗", "text": "hugged"},
    "bite": {"emoji": "😈", "text": "bit"},
    "kiss": {"emoji": "😘", "text": "kissed"},
    "highfive": {"emoji": "🙌", "text": "high-fived"},
    "shoot": {"emoji": "🔫", "text": "shot"},
    "dance": {"emoji": "💃", "text": "danced"},
    "happy": {"emoji": "😊", "text": "was happy"},
    "baka": {"emoji": "😡", "text": "called you a baka"},
    "pat": {"emoji": "👋", "text": "patted"},
    "nod": {"emoji": "👍", "text": "nodded"},
    "nope": {"emoji": "👎", "text": "said nope"},
    "cuddle": {"emoji": "🤗", "text": "cuddled"},
    "feed": {"emoji": "🍴", "text": "fed"},
    "bored": {"emoji": "😴", "text": "was bored"},
    "nom": {"emoji": "😋", "text": "nommed"},
    "yawn": {"emoji": "😪", "text": "yawned"},
    "facepalm": {"emoji": "🤦", "text": "facepalmed"},
    "tickle": {"emoji": "😆", "text": "tickled"},
    "yeet": {"emoji": "💨", "text": "yeeted"},
    "think": {"emoji": "🤔", "text": "thought"},
    "blush": {"emoji": "😊", "text": "blushed"},
    "smug": {"emoji": "😏", "text": "was smug"},
    "wink": {"emoji": "😉", "text": "winked"},
    "peck": {"emoji": "😘", "text": "pecked"},
    "smile": {"emoji": "😄", "text": "smiled"},
    "wave": {"emoji": "👋", "text": "waved"},
    "poke": {"emoji": "👉", "text": "poked"},
    "stare": {"emoji": "👀", "text": "stared"},
    "shrug": {"emoji": "🤷", "text": "shrugged"},
    "sleep": {"emoji": "😴", "text": "slept"},
    "lurk": {"emoji": "👤", "text": "is lurking"},
        "spank": {"emoji": "🍑", "text": "spanked"},
    "lick": {"emoji": "👅", "text": "licked"},
    "straddle": {"emoji": "🔥", "text": "straddled"},
    "tease": {"emoji": "😏", "text": "teased"},
    "snuggle": {"emoji": "🛏️", "text": "snuggled"},
    "flirt": {"emoji": "💘", "text": "flirted with"},
    "moan": {"emoji": "😳", "text": "moaned"},
    "seduce": {"emoji": "🥵", "text": "tried seducing"},
    "handhold": {"emoji": "🤝", "text": "held hands with"},
    "massage": {"emoji": "💆", "text": "gave a massage"},
    "carry": {"emoji": "👐", "text": "carried"},
    "bed": {"emoji": "🛌", "text": "dragged you to bed"},
    "shower": {"emoji": "🚿", "text": "took a shower with"},
    "lapdance": {"emoji": "💃", "text": "gave a lapdance to"},
    "seduce_eye": {"emoji": "👀", "text": "gave a seductive look"},
    "nibble": {"emoji": "🐰", "text": "nibbled"},
    "whisper": {"emoji": "🤫", "text": "whispered something naughty"},
    "cling": {"emoji": "🫂", "text": "clung to"},
    "dominant": {"emoji": "🖤", "text": "went dominant on"},
    "submissive": {"emoji": "🤍", "text": "acted submissive to"},
        "fart": {"emoji": "💨", "text": "farted on"},
    "steal": {"emoji": "👜", "text": "stole from"},
    "boop": {"emoji": "🐽", "text": "booped"},
    "bonk": {"emoji": "🔨", "text": "bonked"},
    "roast": {"emoji": "🔥", "text": "roasted"},
    "simp": {"emoji": "🫡", "text": "simped for"},
    "cry": {"emoji": "😭", "text": "cried for"},
    "explode": {"emoji": "💣", "text": "exploded on"},
    "kick": {"emoji": "🦵", "text": "kicked"},
    "stab": {"emoji": "🗡️", "text": "stabbed"},
    "bury": {"emoji": "⚰️", "text": "buried"},
    "revive": {"emoji": "💉", "text": "revived"},
    "troll": {"emoji": "🧌", "text": "trolled"},
    "boo": {"emoji": "👻", "text": "spooked"},
    "steal_kiss": {"emoji": "💋", "text": "stole a kiss from"},
    "throw": {"emoji": "🪓", "text": "threw at"},
    "ban": {"emoji": "🔨", "text": "banned"},
    "hack": {"emoji": "💻", "text": "hacked"},
    "pizza": {"emoji": "🍕", "text": "shared pizza with"},
    "beer": {"emoji": "🍺", "text": "cheers’d with"},
    "milk": {"emoji": "🥛", "text": "spilled milk on"},
    "chair": {"emoji": "🪑", "text": "hit with a chair"},
    "uwu": {"emoji": "🥺", "text": "went uwu at"},
    "rawr": {"emoji": "🦖", "text": "rawred at"},
    "boom": {"emoji": "🎇", "text": "went boom with"},
    "glare": {"emoji": "😠", "text": "glared at"},
    "flex": {"emoji": "💪", "text": "flexed on"},
        "rose": {"emoji": "🌹", "text": "gave a rose to"},
    "propose": {"emoji": "💍", "text": "proposed to"},
    "date": {"emoji": "🍷", "text": "went on a date with"},
    "holdhands": {"emoji": "🤝", "text": "held hands with"},
    "candlelight": {"emoji": "🕯️", "text": "had a candlelight dinner with"},
    "snuggle": {"emoji": "🛏️", "text": "snuggled with"},
    "valentine": {"emoji": "💘", "text": "asked to be their valentine"},
    "promise": {"emoji": "🤞", "text": "made a promise to"},
    "heart": {"emoji": "❤️", "text": "gave their heart to"},
    "loveletter": {"emoji": "💌", "text": "sent a love letter to"},
    "foreheadkiss": {"emoji": "💏", "text": "kissed your forehead"},
    "warmhug": {"emoji": "🫂", "text": "gave a warm hug to"},
    "caring": {"emoji": "🌸", "text": "cared for"},
    "spoil": {"emoji": "🍫", "text": "spoiled with chocolates"},
    "together": {"emoji": "🌙", "text": "spent the night under the stars with"},
    "dream": {"emoji": "💭", "text": "dreamed about"},
    "serenade": {"emoji": "🎶", "text": "sang a love song for"},
    "cling": {"emoji": "🤍", "text": "clung tightly to"},
    "jealous": {"emoji": "🥺", "text": "got jealous of"},
    "eternal": {"emoji": "♾️", "text": "promised eternal love to"},
        "ignore": {"emoji": "🙄", "text": "ignored"},
    "flex": {"emoji": "💪", "text": "flexed on"},
    "smirk": {"emoji": "😏", "text": "smirked at"},
    "boss": {"emoji": "👑", "text": "showed dominance over"},
    "roast": {"emoji": "🔥", "text": "roasted"},
    "eyeroll": {"emoji": "👀", "text": "rolled eyes at"},
    "reject": {"emoji": "🚫", "text": "rejected"},
    "king": {"emoji": "🤴", "text": "acted like a king in front of"},
    "queen": {"emoji": "👸", "text": "acted like a queen in front of"},
    "ghost": {"emoji": "👻", "text": "ghosted"},
    "block": {"emoji": "⛔", "text": "blocked"},
    "cancel": {"emoji": "❌", "text": "canceled"},
    "thug": {"emoji": "😎", "text": "went full thug mode on"},
    "bossy": {"emoji": "🖕", "text": "showed attitude to"},
    "evilgrin": {"emoji": "😈", "text": "gave an evil grin to"},
    "mock": {"emoji": "😒", "text": "mocked"},
    "sass": {"emoji": "💅", "text": "gave sass to"},
    "kingmove": {"emoji": "♟️", "text": "made a king move on"},
    "rich": {"emoji": "💸", "text": "flexed money on"},

}


def md_escape(text: str) -> str:
    return text.replace('[', '\\[').replace(']', '\\]')


async def get_animation(action: str):
    try:
        result = await neko_client.get_image(action)
        return result.url
    except Exception as e:
        print(f"❌ NekoClient error: {e}")
        return None


@app.on_message(filters.command(list(commands.keys())) & ~filters.forwarded & ~filters.via_bot)
async def animation_command(client: Client, message: Message):
    command = message.command[0].lower()

    if command not in commands:
        return await message.reply_text("⚠️ That command is not supported.")

    gif_url = await get_animation(command)
    if not gif_url:
        return await message.reply_text("❌ Couldn't fetch the animation. Please try again later.")

    sender_name = md_escape(message.from_user.first_name)
    sender = f"[{sender_name}](tg://user?id={message.from_user.id})"

    if message.reply_to_message:
        target_name = md_escape(message.reply_to_message.from_user.first_name)
        target = f"[{target_name}](tg://user?id={message.reply_to_message.from_user.id})"
    else:
        target = sender

    action_text = commands[command]['text']
    emoji = commands[command]['emoji']

    caption = f"**{sender} {action_text} {target}!** {emoji}"

    await message.reply_animation(
        animation=gif_url,
        caption=caption,
        parse_mode=ParseMode.MARKDOWN
    )


















#------------------------------------------------------
@app.on_message(
    filters.command(
        [
            "dice",
            "ludo",
            "dart",
            "basket",
            "basketball",
            "football",
            "slot",
            "bowling",
            "jackpot",
        ]
    )
)
async def dice(c, m: Message):
    command = m.text.split()[0]
    if command == "/dice" or command == "/ludo":

        value = await c.send_dice(m.chat.id, reply_to_message_id=m.id)
        await value.reply_text("ʏᴏᴜʀ sᴄᴏʀᴇ ɪs {0}".format(value.dice.value))

    elif command == "/dart":

        value = await c.send_dice(m.chat.id, emoji="🎯", reply_to_message_id=m.id)
        await value.reply_text("ʏᴏᴜʀ sᴄᴏʀᴇ ɪs {0}".format(value.dice.value))

    elif command == "/basket" or command == "/basketball":
        basket = await c.send_dice(m.chat.id, emoji="🏀", reply_to_message_id=m.id)
        await basket.reply_text("ʏᴏᴜʀ sᴄᴏʀᴇ ɪs {0}".format(basket.dice.value))

    elif command == "/football":
        value = await c.send_dice(m.chat.id, emoji="⚽", reply_to_message_id=m.id)
        await value.reply_text("ʏᴏᴜʀ sᴄᴏʀᴇ ɪs {0}".format(value.dice.value))

    elif command == "/slot" or command == "/jackpot":
        value = await c.send_dice(m.chat.id, emoji="🎰", reply_to_message_id=m.id)
        await value.reply_text("ʏᴏᴜʀ sᴄᴏʀᴇ ɪs {0}".format(value.dice.value))
    elif command == "/bowling":
        value = await c.send_dice(m.chat.id, emoji="🎳", reply_to_message_id=m.id)
        await value.reply_text("ʏᴏᴜʀ sᴄᴏʀᴇ ɪs {0}".format(value.dice.value))


bored_api_url = "https://apis.scrimba.com/bored/api/activity"


@app.on_message(filters.command("bored", prefixes="/"))
async def bored_command(client, message):
    response = requests.get(bored_api_url)
    if response.status_code == 200:
        data = response.json()
        activity = data.get("activity")
        if activity:
            await message.reply(f"𝗙𝗲𝗲𝗹𝗶𝗻𝗴 𝗯𝗼𝗿𝗲𝗱? 𝗛𝗼𝘄 𝗮𝗯𝗼𝘂𝘁:\n\n {activity}")
        else:
            await message.reply("Nᴏ ᴀᴄᴛɪᴠɪᴛʏ ғᴏᴜɴᴅ.")
    else:
        await message.reply("Fᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ ᴀᴄᴛɪᴠɪᴛʏ.")


__MODULE__ = "Fᴜɴ"
__HELP__ = """
**ʜᴀᴠɪɴɢ ꜰᴜɴ:**

• `/dice`: Rᴏʟʟs ᴀ ᴅɪᴄᴇ.
• `/ludo`: Pʟᴀʏ Lᴜᴅᴏ.
• `/dart`: Tʜʀᴏᴡs ᴀ ᴅᴀʀᴛ.
• `/basket` ᴏʀ `/basketball`: Pʟᴀʏs ʙᴀsᴋᴇᴛʙᴀʟʟ.
• `/football`: Pʟᴀʏs ғᴏᴏᴛʙᴀʟʟ.
• `/slot` ᴏʀ `/jackpot`: Pʟᴀʏs ᴊᴀᴄᴋᴘᴏᴛ.
• `/bowling`: Pʟᴀʏs ʙᴏᴡʟɪɴɢ.
• `/bored`: Gᴇᴛs ʀᴀɴᴅᴏᴍ ᴀᴄᴛɪᴠɪᴛʏ ɪғ ʏᴏᴜ'ʀᴇ ʙᴏʀᴇᴅ.
"""


# ©️ Copyright Reserved - @NoxxOP  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @NoxxOP)
# 🔗 GitHub : https://github.com/NoxxOP/HELLBOTS
# 📢 Telegram Channel : https://t.me/ShrutiBots
# ===========================================


# ❤️ Love From ShrutiBots 
