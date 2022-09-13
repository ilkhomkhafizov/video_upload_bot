from aiogram import types
from loader import dp
from filters import IsPrivate
from utils.misc import rate_limit


@rate_limit(limit=15, key='/start')
@dp.message_handler(IsPrivate(), text='/start')
async def start_command(message: types.Message):
    text = f'“Uzbekistan GTL” kompaniyasining oliy ' \
           f'ta’lim muassasalarining iqtidorli ' \
           f'talabalari o‘rtasida o‘tkaziladigan ' \
           f'“GTL stipendiyalar dasturi - 4” ' \
           f'tanlovi uchun maxsus yaratilgan telegram-botga ' \
           f'xush kelibsiz! \n ' \
           f'Registrasiya uchun /register bosing.'
    await message.answer(text)


