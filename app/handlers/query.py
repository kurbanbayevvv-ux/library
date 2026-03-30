from aiogram import Router, types, F
from aiogram.types import CallbackQuery
from database.postgres import getBooks, allBookCount
from aiogram.filters import Command, CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.callback_query(F.data.startswith('page_'))
async def page_query_handler(callback: CallbackQuery):
    page = int(callback.data.replace('page_', ''))
    all_book_count = allBookCount()
    keyb1 = []
    response_text = "Kitoblar:\n\n"
    kitoblar = getBooks(page * 5)

    for i, j in enumerate(kitoblar, start=1 + page * 5):
        response_text += f"{i}. {j[0]}\n"
        keyb1.append(
            InlineKeyboardButton(
                text=str(i),
                callback_data=f"book_{j[1]}"
            )
        )
    keyb = InlineKeyboardMarkup(
        inline_keyboard=[
            keyb1,
            [
                InlineKeyboardButton(text="⬅️", callback_data=f'page_{page - 1}'),
                InlineKeyboardButton(text=f"{page + 1}/{(all_book_count - 1) // 10 + 1}", callback_data='.'),
                InlineKeyboardButton(text="➡️", callback_data=f'page_{page + 1}'),
            ]
        ]
    )
    await callback.message.edit_text(
        text=response_text,
        reply_markup=keyb
    )