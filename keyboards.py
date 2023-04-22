from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


weather = InlineKeyboardButton('Get temperature', callback_data='weather')
exchange_course = InlineKeyboardButton('Currency converter', callback_data='currency_converter')
cute_animal_image = InlineKeyboardButton('Cute animal image', callback_data='cute_animal_image')

command_start_keyboard = InlineKeyboardMarkup(row_width=1).add(weather, exchange_course, cute_animal_image)
