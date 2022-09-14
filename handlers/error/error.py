from aiogram import types
from loader import dp


@dp.message_handler()
async def error_command(message: types.Message):
    text = f'Команда, {message.text} - топилмади'
    await message.answer(text)
