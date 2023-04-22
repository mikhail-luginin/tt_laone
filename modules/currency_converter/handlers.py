from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext

from bot import types

from . import states
from .api import currency_converter


async def currency_converter_handler(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text='Enter your currency')
    await states.CurrencyConverterState.current_currency.set()


async def current_currency_state_handler(message: types.Message, state: FSMContext):
    await state.update_data(dict(current_currency=message.text))
    await message.answer(text='Enter currency for convert')
    await states.CurrencyConverterState.next()


async def currency_for_convert_state_handler(message: types.Message, state: FSMContext):
    await state.update_data(dict(currency_for_convert=message.text))
    await message.answer(text='Enter amount')
    await states.CurrencyConverterState.next()


async def amount_state_handler(message: types.Message, state: FSMContext):
    await state.update_data(dict(amount=message.text))

    data = await state.get_data()

    await message.answer(text=await currency_converter(current_currency=data.get('current_currency'),
                                                       currency_for_convert=data.get('currency_for_convert'),
                                                       amount=data.get('amount')))
    await state.finish()


def register_currency_converter_handlers(dispatcher: Dispatcher) -> None:
    callback_query_handlers = [
        dict(callback=currency_converter_handler, text='currency_converter')
    ]

    state_handlers = [
        dict(callback=current_currency_state_handler, state=states.CurrencyConverterState.current_currency),
        dict(callback=currency_for_convert_state_handler, state=states.CurrencyConverterState.currency_for_convert),
        dict(callback=amount_state_handler, state=states.CurrencyConverterState.amount)
    ]

    for handler in callback_query_handlers:
        dispatcher.register_callback_query_handler(**handler)

    for handler in state_handlers:
        dispatcher.register_message_handler(**handler)
