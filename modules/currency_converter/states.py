from aiogram.dispatcher.filters.state import StatesGroup, State


class CurrencyConverterState(StatesGroup):
    current_currency = State()
    currency_for_convert = State()
    amount = State()
