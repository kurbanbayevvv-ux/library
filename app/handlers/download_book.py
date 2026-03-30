from aiogram import types, Router, F
from aiogram.types import CallbackQuery
from dotenv import load_dotenv
import os

from aiogram import Bot

load_dotenv()

router = Router()

@router.callback_query(F.data.startswith('book_'))
async def download_book_query_handlers(callback: types.CallbackQuery, bot: Bot):
    book_id = int(callback.data.replace('book_', ''))
    await bot.copy_message(
        chat_id=callback.from_user.id,
        from_chat_id=os.getenv('CHANNEL_ID'),
        message_id=book_id
    )