from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○   Oᴡɴᴇʀ - </b> <a href='tg://user?id={OWNER_ID}'>Mᴏɴᴋᴇʏ D Lᴜғғʏ</a> \n<b>○   Dᴇᴠᴇʟᴏᴘᴇʀ - </b> <a href='https://t.me/abidabdullah199'>Cʟɪᴄᴋ Hᴇʀᴇ</a> \n<b>○   Cʜᴀɴɴᴀʟ - </b> <a href='https://t.me/AnimeQuestX'>Aɴɪᴍᴇ Qᴜᴇsᴛ</a> \n<b>○   Dᴏɴɢʜᴜᴀ Cʜᴀɴɴᴀʟ - </b> <a href='https://t.me/DonghuaQuest'>Jᴏɪɴ Nᴏᴡ</a> \n<b>○   Oɴɢᴏɪɴɢ Cʜᴀɴɴᴀʟ - </b> <a href='https://t.me/OngoingAnimeQuest'>Jᴏɪɴ Nᴏᴡ</a> \n<b>○   Dɪsᴄᴜssᴛɪᴏɴ Gʀᴏᴜᴘ - </b> <a href='https://t.me/AnimeQuestChat'>Jᴏɪɴ Nᴏᴡ</a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡Cʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('⛄Aɴɪᴍᴇ Qᴜᴇsᴛ', url='https://t.me/AnimeQuestX')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
