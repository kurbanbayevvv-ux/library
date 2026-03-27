import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

# from handlers.register import router as register
# from handlers.admin import router as admin
# from handlers.menu import router as menu
from handlers.start import router as start_router
from handlers.download_book import router as download_book_router

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(download_book_router)
    # dp.include_router(register)
    # dp.include_router(admin)
    # dp.include_router(menu)

    print("Bot ishga tushdi...")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())