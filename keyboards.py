from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


weather = InlineKeyboardButton('Get temperature', callback_data='weather')
exchange_course = InlineKeyboardButton('Currency converter', callback_data='currency_converter')

command_start_keyboard = InlineKeyboardMarkup(row_width=1).add(weather, exchange_course)
