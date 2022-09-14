def check_admin(func):

    async def wrapper(message):
        user = await register_commands.select_user_by_id(user_id=message.chat.id)
        if user:
            if not user.is_admin:
                print("admin emas")
                return await message.reply("Siz Admin emassiz")
            return await func(message)
        return await message.reply("Siz Admin emas!")

    return wrapper
