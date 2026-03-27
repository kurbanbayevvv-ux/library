from aiogram import Router, types, F
from keyboards.keyboards import keyboard_admin_panel
from aiogram import Bot

router = Router()

@router.message(F.text == "Admin panel")
async def admin_handler(message: types.Message):
    await message.answer("*ADMIN*", parse_mode="markdown", reply_markup=keyboard_admin_panel)
