from aiogram.utils.exceptions import BotKicked

from typing import List


def get_options(options: str) -> List[str]:
    return [option.strip() for option in options.split(',')]


async def create_poll(data: dict) -> str:
    from bot import bot

    chat_id = data.get('chat_id')
    question = data.get('question')
    poll_type = data.get('poll_type')
    is_anonymous = data.get('is_anonymous')
    allows_multiple_answers = poll_type == 'multiple'
    options = data.get('options')
    correct_option = data.get('correct_option')

    poll = {
        "question": question,
        "type": "regular" if allows_multiple_answers else poll_type,
        "is_anonymous": is_anonymous,
        "allows_multiple_answers": allows_multiple_answers,
        "options": options,
        "correct_option_id": correct_option if correct_option is not None else None
    }

    try:
        await bot.send_poll(chat_id, **poll)
        return 'Poll was successfully created :)'
    except BotKicked:
        return 'Bot is not in this group :('
