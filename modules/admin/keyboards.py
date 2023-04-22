from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ANONYMOUS = InlineKeyboardButton('Anonymous', callback_data='anonymous')
NOT_ANONYMOUS = InlineKeyboardButton('Not anonymous', callback_data='not_anonymous')

choose_anonymous_keyboard = InlineKeyboardMarkup(row_width=2).add(ANONYMOUS, NOT_ANONYMOUS)


REGULAR = InlineKeyboardButton('Regular', callback_data='regular')
MULTIPLE = InlineKeyboardButton('Multiple questions', callback_data='multiple')
QUIZ = InlineKeyboardButton('Quiz', callback_data='quiz')

choose_question_pool_keyboard = InlineKeyboardMarkup(row_width=3).add(REGULAR, MULTIPLE, QUIZ)
