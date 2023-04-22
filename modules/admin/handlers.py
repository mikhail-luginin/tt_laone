from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext

from bot import types

from . import validators
from . import states


async def add_admin_handler(message: types.Message):
    sender_username = message.from_user.username

    validate_status = await validators.validate_is_admin(sender_username)

    if validate_status:
        await message.answer(text='Enter username for add to admin list')
        await states.AddAdminState.add_admin.set()


async def add_admin_state(message: types.Message, state: FSMContext):
    with open('modules/admin/admins.txt', 'a') as file:
        file.write('\n' + message.text)

    await message.answer(text='Administrator was successfully added :)')
    await state.finish()


async def add_photo_handler(message: types.Message):
    sender_username = message.from_user.username

    validate_status = await validators.validate_is_admin(sender_username)

    if validate_status:
        await message.answer(text='Enter photo url')
        await states.AddPhotoState.add_photo.set()


async def add_photo_state(message: types.Message, state: FSMContext):
    if await validators.validate_is_link(message.text):
        if await validators.validate_is_photo(message.text):
            with open('modules/random_images/photo_urls.txt', 'a') as file:
                file.write('\n' + message.text)
            await message.answer(text='Photo was successfully added :)')
        else:
            await message.answer(text='This link does not contain photo :(')
    else:
        await message.answer(text='Your message is not link :(')
    await state.finish()


def register_admin_handlers(dispatcher: Dispatcher) -> None:
    message_handlers = [
        dict(callback=add_admin_handler, commands=['add_admin']),
        dict(callback=add_admin_state, state=states.AddAdminState.add_admin),

        dict(callback=add_photo_handler, commands=['add_photo']),
        dict(callback=add_photo_state, state=states.AddPhotoState.add_photo)
    ]

    for handler in message_handlers:
        dispatcher.register_message_handler(**handler)
