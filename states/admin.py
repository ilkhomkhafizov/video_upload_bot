from aiogram.dispatcher.filters.state import StatesGroup, State


class Admin(StatesGroup):
    password = State()
