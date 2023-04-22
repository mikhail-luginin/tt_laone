from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext

from bot import types, bot

from . import validators, states, keyboards, services


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


async def create_poll_handler(message: types.Message):
    await message.answer('Enter question for poll')
    await states.PollCreatingState.question.set()


async def poll_question_state_handler(message: types.Message, state: FSMContext):
    await state.update_data(dict(question=message.text))
    await message.answer('Is your poll anonymous?', reply_markup=keyboards.choose_anonymous_keyboard)
    await states.PollCreatingState.next()


async def poll_is_anonymous_state_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(dict(is_anonymous=callback_query.data == 'anonymous'))
    await callback_query.message.answer('Enter your variables separated by commas (cat, dog etc.)')
    await states.PollCreatingState().next()


async def poll_options_state_handler(message: types.Message, state: FSMContext):
    await state.update_data(dict(options=services.get_options(message.text)))
    await message.answer('Enter poll explantation')
    await states.PollCreatingState.next()


async def poll_explantation_state_handler(message: types.Message, state: FSMContext):
    await state.update_data(dict(explantation=message.text))
    await message.answer('Choose poll type', reply_markup=keyboards.choose_question_pool_keyboard)
    await states.PollCreatingState.next()


async def poll_type_state_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(dict(poll_type=callback_query.data))
    data = await state.get_data()
    await services.create_poll(bot, data)
    await callback_query.message.answer('Poll successfully created')
    await state.finish()


def register_admin_handlers(dispatcher: Dispatcher) -> None:
    message_handlers = [
        dict(callback=add_admin_handler, commands=['add_admin']),
        dict(callback=add_admin_state, state=states.AddAdminState.add_admin),

        dict(callback=add_photo_handler, commands=['add_photo']),
        dict(callback=add_photo_state, state=states.AddPhotoState.add_photo),

        dict(callback=create_poll_handler, commands=['create_poll']),
        dict(callback=poll_question_state_handler, state=states.PollCreatingState.question),
        dict(callback=poll_explantation_state_handler, state=states.PollCreatingState.explantation),
        dict(callback=poll_options_state_handler, state=states.PollCreatingState.options)
    ]

    callback_query_handlers = [
        dict(callback=poll_is_anonymous_state_handler, state=states.PollCreatingState.is_anonymous),
        dict(callback=poll_type_state_handler, state=states.PollCreatingState.poll_type)
    ]

    for handler in message_handlers:
        dispatcher.register_message_handler(**handler)

    for handler in callback_query_handlers:
        dispatcher.register_callback_query_handler(**handler)
