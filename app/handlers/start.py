from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.postgres import getBooks, allBookCount

router= Router()

@router.message(CommandStart())
async def start_handler(message: types.Message):
    all_book_count = allBookCount()
    keyb1 = []
    response_text = "Kitoblar:\n\n"
    kitoblar = getBooks(0)

    for i, j in enumerate(kitoblar, start=1):
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
                InlineKeyboardButton(text="⬅️", callback_data='page_-1'),
                InlineKeyboardButton(text=f"10/{all_book_count}", callback_data='.'),
                InlineKeyboardButton(text="➡️", callback_data='page_1'),
            ]
        ]
    )
    await message.answer(
        text=response_text,
        reply_markup=keyb
    )


@router.message(Command('preview'))
async def preview_handler(message: types.Message):
    response_text = ("Kitoblar:\n\n"
                     "1. Umar Xayyom Ruboiylar\n"
                     "2. Matematika\n"
                     "3. Dasturlash asoslari\n"
                     "4. Geografiya\n"
                     "5. Ingliz tili\n"
                     "6. Nemis tili\n"
                     "7. Geometriya\n"
                     "8. Rus tili\n"
                     "9. Fizika asoslari\n"
                     "10. Adabiyot")
    keyb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="1", callback_data='book_1'),
                InlineKeyboardButton(text="2", callback_data='book_2'),
                InlineKeyboardButton(text="3", callback_data='book_3'),
                InlineKeyboardButton(text="4", callback_data='book_4'),
                InlineKeyboardButton(text="5", callback_data='book_5'),
            ],
            [
                InlineKeyboardButton(text="6", callback_data='book_6'),
                InlineKeyboardButton(text="7", callback_data='book_7'),
                InlineKeyboardButton(text="8", callback_data='book_8'),
                InlineKeyboardButton(text="9", callback_data='book_9'),
                InlineKeyboardButton(text="10", callback_data='book_10'),
            ],
            [
                InlineKeyboardButton(text="⬅️", callback_data='page_-1'),
                InlineKeyboardButton(text="10/24", callback_data='.'),
                InlineKeyboardButton(text="➡️", callback_data='page_1'),
            ]
        ]
    )
    await message.answer(
        text=response_text,
        reply_markup=keyb
    )