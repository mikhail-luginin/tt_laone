from aiogram import types
from aiogram.dispatcher import FSMContext

from . import validators


async def check_admin(handler):
    async def wrapped(message: types.Message, state: FSMContext):
        sender_username = message.from_user.username
        validate_status = await validators.validate_is_admin(sender_username)
        await message.answer(text='You are not admin :(') if not validate_status else await handler(message, state)
    return wrapped
