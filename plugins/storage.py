#Nothing is here


































@Bot.on_message(filters.command("dev"))
async def dev_command(client: Bot, message: Message):
    await message.reply_text(
        text = f"<b>○   Oᴡɴᴇʀ - </b> <a href='tg://user?id={OWNER_ID}'>Mᴏɴᴋᴇʏ D Lᴜғғʏ</a> \n<b>○   Dᴇᴠᴇʟᴏᴘᴇʀ - </b> <a href='https://t.me/abidabdullah199'>Aɴɪᴍᴇ Qᴜᴇsᴛ</a> \n<b>\n<b>○   Cʜᴀɴɴᴀʟ - </b> <a href='https://t.me/AnimeQuestX'>Aɴɪᴍᴇ Qᴜᴇsᴛ</a> \n<b>○   Dᴏɴɢʜᴜᴀ Cʜᴀɴɴᴀʟ - </b> <a href='https://t.me/DonghuaQuest'>Jᴏɪɴ Nᴏᴡ</a> \n<b>○   Oɴɢᴏɪɴɢ Cʜᴀɴɴᴀʟ - </b> <a href='https://t.me/OngoingAnimeQuest'>Jᴏɪɴ Nᴏᴡ</a> \n<b>○   Dɪsᴄᴜssᴛɪᴏɴ Gʀᴏᴜᴘ - </b> <a href='https://t.me/AnimeQuestChat'>Jᴏɪɴ Nᴏᴡ</a>",
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

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
