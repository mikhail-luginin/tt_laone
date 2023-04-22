from aiogram import Dispatcher

import aiohttp

from bot import types, bot
from .services import get_random_photo_url


async def send_image_handler(callback_query: types.CallbackQuery):
    photo_url = await get_random_photo_url()
    chat_id = callback_query.message.chat.id

    if photo_url is False:
        await bot.send_message(chat_id=chat_id, text='Sorry, but our bot dont have photos now :(')
    else:
        async with aiohttp.ClientSession() as session:
            async with session.get(photo_url, ssl=False) as resp:
                await bot.send_photo(chat_id=chat_id, photo=resp.content)


def register_random_images_handlers(dispatcher: Dispatcher) -> None:
    callback_query_handlers = [
        dict(callback=send_image_handler, text='cute_animal_image')
    ]

    for handler in callback_query_handlers:
        dispatcher.register_callback_query_handler(**handler)
