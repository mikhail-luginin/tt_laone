from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext

from bot import types

from . import messages
from . import states


async def weather(callback_query: types.CallbackQuery):
    await states.WeatherState.country.set()
    await callback_query.answer(text='Enter the city where you want to know the current weather',
                                show_alert=True)


async def city(message: types.Message, state: FSMContext):
    await message.answer(text=await messages.get_temperature(message.text))
    await state.finish()


def register_weather_handlers(dispatcher: Dispatcher) -> None:
    callback_query_handlers = [
        dict(callback=weather, text='weather')
    ]

    state_handlers = [
        dict(callback=city, state=states.WeatherState.country)
    ]

    for handler in callback_query_handlers:
        dispatcher.register_callback_query_handler(**handler)

    for handler in state_handlers:
        dispatcher.register_message_handler(**handler)
