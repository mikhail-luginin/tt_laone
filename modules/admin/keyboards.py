from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ANONYMOUS = InlineKeyboardButton('Anonymous', callback_data='anonymous')
NOT_ANONYMOUS = InlineKeyboardButton('Not anonymous', callback_data='not_anonymous')

choose_anonymous_keyboard = InlineKeyboardMarkup(row_width=2).add(ANONYMOUS, NOT_ANONYMOUS)


REGULAR = InlineKeyboardButton('Regular', callback_data='regular')
MULTIPLE = InlineKeyboardButton('Multiple', callback_data='multiple')
QUIZ = InlineKeyboardButton('Quiz', callback_data='quiz')

choose_question_pool_keyboard = InlineKeyboardMarkup(row_width=3).add(REGULAR, MULTIPLE, QUIZ)


async def generate_inline_keyboard(buttons: list):
    return InlineKeyboardMarkup(row_width=2).add(*[InlineKeyboardButton(btn_text, callback_data=str(index)) for index, btn_text in enumerate(buttons)])
