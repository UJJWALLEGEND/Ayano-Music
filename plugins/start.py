from modules.config import (
    START_PIC, 
    BOT_USERNAME,
    SUPPORT_GROUP,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
)
from modules.helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message



@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_private(client: Client, message: Message):
 await message.reply_photo(
        photo=f"{START_PIC}",
        caption=f"""**💥 𝐇𝐞𝐥𝐥𝐨, 𝐈 𝐚𝐦 𝐒𝐮𝐩𝐞𝐫𝐟𝐚𝐬𝐭 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲
𝐍𝐨 𝐋𝐚𝐠 𝐕𝐂 𝐌𝐮𝐬𝐢𝐜 𝐏𝐥𝐚𝐲𝐞𝐫 𝐁𝐨𝐭 💞 𝐉𝐮𝐬𝐭 𝐀𝐝𝐝 𝐌𝐞 » 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝
𝐄𝐧𝐣𝐨𝐲 𝐒𝐮𝐩𝐞𝐫 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 ❥︎𝐌𝐮𝐬𝐢𝐜.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton("✨𝙊𝙒𝙉𝜩𝙍'𝐱𝐃🥀", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton("🖤 𝘿𝜩𝙑𝙀𝙇𝙊𝙋𝜩𝙍'𝐱𝐃 💥", url=f"https://t.me/MAGNESIUM_XD"),
                ],
                [
                    InlineKeyboardButton(
                        "💻𝑆𝑈𝑃𝑃𝑂𝑅𝑇•𝐶𝐻𝐴𝑇💌", url=f"{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "🥀𝙐𝙋𝘿𝘼𝙏𝜩𝙎•𝘾𝙃𝘼𝙉𝙉𝜩𝙇📡", url=f"{UPDATES_CHANNEL}"
                    ),
                ],
            ]
        ),
    )


