from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.user import User


async def add_user(user_id: int, full_name: str, university: str, phone: str, video: str):
    try:
        user = User(user_id=user_id, full_name=full_name, university=university, phone=phone, video=video)
        await user.create()
    except UniqueViolationError:
        print("Пользователь не добавлен")


async def select_user_by_id(user_id: int):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user
