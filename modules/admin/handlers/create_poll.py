from aiogram import types
from aiogram.dispatcher import FSMContext

from .. import states, keyboards, services
from ..decorators import check_admin


@check_admin
async def create_poll_command_handler(message: types.Message):
    """
    This handler called after command /create_poll and used for start PollCreatingState.

    :param message:
    :type message: types.Message

    :return:
    """

    await message.answer('Enter id of chat where the poll will be sent (for example: -12929191, 192929191 etc.)')
    await states.PollCreatingState.chat_id.set()


async def poll_chat_id_state_handler(message: types.Message, state: FSMContext):
    """
    :param message:
    :type message: types.Message

    :param state:
    :type state: FSMContext

    :return:
    """

    async with state.proxy() as data:
        data['chat_id'] = message.text
    await message.answer('Enter question for poll')
    await states.PollCreatingState.next()


async def poll_question_state_handler(message: types.Message, state: FSMContext):
    """
    :param message:
    :type message: types.Message

    :param state:
    :type state: FSMContext

    :return:
    """

    async with state.proxy() as data:
        data['question'] = message.text
    await message.answer('Is your poll anonymous?', reply_markup=keyboards.choose_anonymous_keyboard)
    await states.PollCreatingState.next()


async def poll_is_anonymous_state_handler(callback_query: types.CallbackQuery, state: FSMContext):
    """
    :param callback_query:
    :type callback_query: types.CallbackQuery

    :param state:
    :type state: FSMContext

    :return:
    """

    async with state.proxy() as data:
        data['is_anonymous'] = callback_query.data == 'anonymous'
    await callback_query.message.answer('Enter your variables separated by commas (cat, dog etc.)')
    await states.PollCreatingState().next()


async def poll_options_state_handler(message: types.Message, state: FSMContext):
    """
    :param message:
    :type message: types.Message

    :param state:
    :type state: FSMContext

    :return:
    """

    async with state.proxy() as data:
        data['options'] = services.get_options(message.text)
    await message.answer('Choose poll type', reply_markup=keyboards.choose_question_pool_keyboard)
    await states.PollCreatingState.next()


async def poll_type_state_handler(callback_query: types.CallbackQuery, state: FSMContext):
    """
    :param callback_query:
    :type callback_query: types.CallbackQuery

    :param state:
    :type state: FSMContext

    :return:
    """

    poll_type = callback_query.data
    async with state.proxy() as data:
        data['poll_type'] = poll_type

    data = await state.get_data()

    if poll_type == 'quiz':
        keyboard = await keyboards.generate_inline_keyboard(data['options'])
        await callback_query.message.answer('Choose correct option', reply_markup=keyboard)
        await states.PollCreatingState.next()

    result = await services.create_poll(data)
    await callback_query.message.answer(result)
    await state.finish()


async def poll_correct_option_state_handler(callback_query: types.CallbackQuery, state: FSMContext):
    """

    :param callback_query:
    :type callback_query: types.CallbackQuery

    :param state:
    :type state: FSMContext

    :return:
    """

    async with state.proxy() as data:
        data['correct_option'] = callback_query.data

    data = await state.get_data()
    result = await services.create_poll(data)
    await callback_query.message.answer(result)
    await state.finish()
