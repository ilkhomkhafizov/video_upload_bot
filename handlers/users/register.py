from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from filters import IsPrivate
from loader import dp
from states import User
from utils.db_api import register_commands


@dp.message_handler(IsPrivate(), Command('register'))
async def register_command(message: types.Message):
    text = f'Stipendiya dasturi ishtirokchisining ismi, \n' \
           f'familiyasi va otasining ismi:'
    await message.answer(text)
    await User.full_name.set()


@dp.message_handler(IsPrivate(), state=User.full_name)
async def fio_command(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(full_name=answer)
    text = f'Stipendiya dasturi ishtirokchisi tahsil olayotgan \n ' \
           f'oliy ta’lim muassasasining nomi:'
    await message.answer(text)
    await User.university.set()


@dp.message_handler(IsPrivate(), state=User.university)
async def university_command(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(university=answer)
    text = f'Stipendiya dasturi ishtirokchisining telefon raqami:'
    await message.answer(text)
    await User.phone.set()


@dp.message_handler(IsPrivate(), state=User.phone)
async def phone_command(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(phone=answer)
    text = f'Tanlov shartlariga muvofiq, tanlov hay’atiga o‘zingiz haqingizda \n ' \
           f'to‘liqroq ma’lumot va tasavvur qoldirish imkonini beruvchi videorolik \n' \
           f'yuborishingiz mumkin'
    await message.answer(text)
    await User.video.set()


@dp.message_handler(IsPrivate(), state=User.video, content_types=types.ContentTypes.VIDEO)
async def video_command(message: types.Message, state: FSMContext):
    video_id = message.video.file_id
    await state.update_data(video=video_id)
    text = f'Siz qoldirgan ma’lumotlar va videorolik qabul qilindi. \n ' \
           f'Stipendiya dasturidagi ishtirokingiz uchun minnatdorchilik bildiramiz!'
    data = await state.get_data()
    full_name = data.get('full_name')
    university = data.get('university')
    phone = data.get('phone')
    video = data.get('video')
    await register_commands.add_user(user_id=message.from_user.id, full_name=full_name, university=university,
                                     phone=phone, video=video)

    await state.finish()
    await message.answer(text)

