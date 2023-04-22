from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import logging
import config

from modules import register_all_handlers
from keyboards import command_start_keyboard

logging.basicConfig(filename='logs/errors.txt', level=logging.ERROR)
logging.basicConfig(filename='logs/warnings.txt', level=logging.WARNING)
logging.basicConfig(filename='logs/info.txt', level=logging.INFO)

bot = Bot(token=config.TELEGRAM_API_KEY)
dp = Dispatcher(bot, storage=MemoryStorage())


async def __on_start_up(dispatcher: Dispatcher) -> None:
    register_all_handlers(dispatcher)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.chat.id, f'Welcome, {message.from_user.username}.\n'
                                            f'Choose function..',
                           reply_markup=command_start_keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)
