from aiogram import Router, types, F, Bot
from aiogram.types import MessageOriginChannel

router = Router()

@router.channel_post()
async def book_save_handler(message: types.MessageOriginChannel, bot: Bot):
    await bot.send_message(chat_id=603911289, text=str(message.type))