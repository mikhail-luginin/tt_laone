def get_options(options: str) -> list:
    return [option.strip() for option in options.split(',')]


async def create_poll(bot, data: dict) -> None:
    poll = dict(
        question=data['question'],
        type=data['poll_type'],
        is_anonymous=data['is_anonymous'],
        options=data['options'],
        explanation=data['explantation']
    )
    await bot.send_poll('-900690534', **poll)

