from aiogram import Router, types, F, Bot
from aiogram.types import MessageOriginChannel
from database.postgres import saveBook
router = Router()

@router.channel_post()
async def book_save_handler(message: types.MessageOriginChannel, bot: Bot):
    saveBook(message.document.file_name, message.message_id)