from aiogram import types

from . import validators


def check_admin(handler):
    async def wrapped(message: types.Message, *args, **kwargs):
        sender_username = message.from_user.username
        validate_status = await validators.validate_is_admin(sender_username)
        await message.answer(text='You are not admin :(') if not validate_status else await handler(message,
                                                                                                    *args, **kwargs)
    return wrapped
