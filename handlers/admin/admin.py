from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data.config import ADMIN_PASSWORD
from loader import dp
from filters import IsPrivate
from states.admin import Admin
from utils.db_api import register_commands as commands


@dp.message_handler(IsPrivate(), Command('admin'))
async def admin_command(message: types.Message):
    text = f'Admin parol:'
    await message.answer(text)
    await Admin.password.set()


@dp.message_handler(IsPrivate(), state=Admin.password)
async def check_admin_command(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(password=answer)
    if answer == ADMIN_PASSWORD:
        users = await commands.select_all_users()
        if len(users) > 0:
            for user in users:
                full_name = user.full_name
                phone = user.phone
                video = user.video
                await dp.bot.send_video(chat_id=message.chat.id, video=video,
                                        caption=f"{full_name} - {phone}")
    else:
        await message.answer("Parol noto'g'ri")
    await state.finish()
