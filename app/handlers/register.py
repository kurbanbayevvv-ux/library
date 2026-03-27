from keyboards.keyboards import keyboard_start, keyboard_phone_number
from database.postgres import Register as RegisterUser, addUserInfo
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram import Router, types, Bot, F
from states.register import Register
from dotenv import load_dotenv
import os

load_dotenv()

admin = os.getenv("ADMIN")
isAdmin = lambda x: os.getenv('ADMIN') == str(x)

router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message):
    chatId = message.chat.id
    firstName = message.chat.first_name

    RegisterUser(chat_id=chatId, first_name=firstName)

    await message.answer(
        f"Salom xush kelibsiz! {firstName}",
        reply_markup=keyboard_start(isAdmin(chatId))
    )


@router.message(lambda msg: msg.text == "Ro'yxatdan o'tish")
async def reg_start(message: types.Message, state: FSMContext):
    await message.answer("Ismingizni kiriting:")
    await state.set_state(Register.name)


@router.message(Register.name)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)

    await message.answer(
        "Telefon raqamingizni yuboring:",
        reply_markup=keyboard_phone_number
    )
    await state.set_state(Register.phone)


@router.message(Register.phone)
async def get_phone(message: types.Message, state: FSMContext):
    if message.contact:
        phone = message.contact.phone_number
    else:
        phone = message.text

    data = await state.update_data(phone=phone)

    name = data["name"]

    await message.answer(
        await message.answer(f"🎉 Botga xush kelibsiz, {name}!")
    )

    chatId = message.chat.id
    addUserInfo(chatId, name, phone)

    BOT_TOKEN = os.getenv("BOT_TOKEN")
    bot = Bot(token=BOT_TOKEN)

    await bot.send_message(
        chat_id=admin,
        text=f"Yangi foydalanuvchi:\n"
             f"Ism: {name}\n"
             f"Tel: {phone}"
    )

    await state.clear()