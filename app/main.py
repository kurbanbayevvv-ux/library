import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers.start import router as start_router
from handlers.query import router as query_router
from handlers.download_book import router as download_book_router
from handlers.book_channel import router as book_channel_router

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # router ulash
    dp.include_router(start_router)
    dp.include_router(query_router)
    dp.include_router(download_book_router)
    dp.include_router(book_channel_router)

    print("Bot ishga tushdi...")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())