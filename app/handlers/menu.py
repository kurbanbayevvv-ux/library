from http.client import responses

from aiogram import F, Router, types
from aiogram.types import CallbackQuery, InlineKeyboardButton
from database.postgres import getUsers
from database.postgres import countUsers
from database.postgres import getUser
from keyboards.keyboards import test_keyboard
from aiogram.types import InlineKeyboardMarkup
router = Router()


@router.callback_query(F.data =='users')
async  def users_query_handlers(callback: types.CallbackQuery):
    users = getUsers()
    response_text = ""
    for user in users:
        response_text += f"{user[1]} {user[2]}\n"
    await callback.message.answer("Foydalanuvchilar:\n"+str(response_text))


@router.callback_query(F.data == 'count_users')
async def count_users_query_handler(callback: types.CallbackQuery):
    count_users = countUsers()
    await callback.message.answer(f"Foydalanuvchilar soni : {count_users}")

@router.callback_query(F.data == 'userss')
async def userss_query_handler(callback: types.CallbackQuery):
    user = getUser(0)
    response_text =(f"<b>Foydalanuvchi:</b>\n"
                    f"<b>id:</b> {user[0]}\n"
                    f"<b>telegram nomi:</b> {user[1]}\n"
                    f"<b>Telefon raqami:</b> {user[2]}\n")
    count_user = countUsers()
    text_count_user = f"1/{count_user}"
    await callback.message.edit_text(
        text=response_text,
        parse_mode='html',
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text = '<', callback_data=f"page_-1"),
                    InlineKeyboardButton(text=text_count_user, callback_data='count_user'),
                    InlineKeyboardButton(text = '>', callback_data=f"page_1")
                ]
            ]

        )
    )
    
@router.callback_query(F.data.startswith('page_'))
async def left_user_query_handler(callback: types.CallbackQuery):
    page = int(callback.data.replace('page_', ''))
    user = getUser(page)
    count_user = countUsers()
    response_text =(f"<b>Foydalanuvchi:</b>\n"
                    f"<b>id:</b> {user[0]}\n"
                    f"<b>telegram nomi:</b> {user[2]}\n"
                    f"<b>Telefon raqami:</b> {user[3]}\n")

    text_count_user = f"{page+1}/{count_user}"
    await callback.message.edit_text(
        text=response_text,
        parse_mode='html',
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='<', callback_data=f"page_{page - 1}"),
                    InlineKeyboardButton(text=text_count_user, callback_data='count_user'),
                    InlineKeyboardButton(text='>', callback_data=f"page_{page + 1}")]
            ]

        )
    )
