from aiogram.dispatcher.filters.state import StatesGroup, State


class User(StatesGroup):
    full_name = State()
    university = State()
    phone = State()
    video = State()
