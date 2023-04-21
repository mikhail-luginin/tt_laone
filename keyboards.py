from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


weather = InlineKeyboardButton('Узнать погоду', callback_data='weather')
exchange_course = InlineKeyboardButton('Конвертировать валюту', callback_data='currency_converter')

command_start_keyboard = InlineKeyboardMarkup().add(weather, exchange_course)
