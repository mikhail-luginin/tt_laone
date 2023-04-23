from aiogram import types
from aiogram.dispatcher import FSMContext

from .. import validators, states, decorators


async def add_photo_command_handler(message: types.Message):
    """
    This handler called after command /add_photo and used for start AddPhotoState.

    :param message:
    :type message: types.Message

    :return:
    """

    await message.answer(text='Enter photo url (for example: https://i.imgur.com/asd.png)')
    await states.AddPhotoState.add_photo.set()


@decorators.check_admin
async def add_photo_state_handler(message: types.Message, state: FSMContext):
    """
    This handler used for add photo url to photo urls list.

    :param message:
    :type message: types.Message

    :param state:
    :type state: FSMContext

    :return:
    """

    try:
        async with state.proxy() as data:
            data['photo_url'] = message.text
            if not await validators.validate_is_link(data['photo_url']):
                raise ValueError('Your message is not link :(')
            if not await validators.validate_is_photo(data['photo_url']):
                raise ValueError('This link does not contain photo :(')
            with open('modules/random_images/photo_urls.txt', 'a') as file:
                file.write('\n' + data['photo_url'])
            await message.answer(text='Photo was successfully added :)')
            await state.finish()
    except ValueError as e:
        await message.answer(text=str(e))
