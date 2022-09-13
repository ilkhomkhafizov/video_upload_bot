async def on_startup(dp):
    import filters
    filters.setup(dp)

    import middleware
    middleware.setup(dp)

    from loader import db
    from utils.db_api.db_gino import on_startup
    await on_startup(dp)
    print('Подключились к бд')

    await db.gino.drop_all()
    print('Удалили все из бд')
    await db.gino.create_all()
    print('Создали таблицу в бд')

    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)

    print("Бот запущен")


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
