from aiogram import types
from aiogram.dispatcher import FSMContext

from .. import states, keyboards, services


async def create_poll_command_handler(message: types.Message):
    """
    This handler called after command /create_poll and used for start PollCreatingState.

    :param message:
    :type message: types.Message

    :return:
    """

    await message.answer('Enter question for poll')
    await states.PollCreatingState.question.set()


async def poll_question_state_handler(message: types.Message, state: FSMContext):
    """
    :param message:
    :type message: types.Message

    :param state:
    :type state: FSMContext

    :return:
    """

    await state.update_data(dict(question=message.text))
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

    await state.update_data(dict(is_anonymous=callback_query.data == 'anonymous'))
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

    await state.update_data(dict(options=services.get_options(message.text)))
    await message.answer('Enter poll explantation')
    await states.PollCreatingState.next()


async def poll_explantation_state_handler(message: types.Message, state: FSMContext):
    """
    :param message:
    :type message: types.Message

    :param state:
    :type state: FSMContext

    :return:
    """

    await state.update_data(dict(explantation=message.text))
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

    await state.update_data(dict(poll_type=callback_query.data))
    data = await state.get_data()
    await services.create_poll(data)
    await callback_query.message.answer('Poll successfully created')
    await state.finish()
