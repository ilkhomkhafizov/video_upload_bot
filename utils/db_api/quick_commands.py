from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.user import User


async def add_user(user_id: int, full_name: str, university: str, age: int):
    try:
        user = User(user_id=user_id, full_name=full_name, university=university, age=age)
        await user.create()
    except UniqueViolationError:
        print("Пользователь не добавлен")


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def count_users():
    count = await db.func.count(User.user_id).gino.scalar()
    return count


async def select_user_by_id(user_id: int):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user
