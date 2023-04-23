from typing import List


def get_options(options: str) -> List[str]:
    return [option.strip() for option in options.split(',')]


async def create_poll(data: dict) -> None:
    from bot import bot

    poll = dict(
        question=data['question'],
        type=data['poll_type'],
        is_anonymous=data['is_anonymous'],
        options=data['options'],
        explanation=data['explantation']
    )
    await bot.send_poll(data['chat_id'], **poll)
