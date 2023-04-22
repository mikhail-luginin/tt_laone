import random


async def get_random_photo_url() -> str | bool:
    file = open('modules/random_images/photo_urls.txt', 'r')
    lines = [line.strip() for line in file if line.strip() != '']

    return random.choice(lines) if len(lines) > 0 else False
