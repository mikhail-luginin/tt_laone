async def validate_is_admin(username: str) -> bool:
    with open('modules/admin/admins.txt', 'r') as file:
        lines = [line.strip() for line in file]

    return username in lines


async def validate_is_photo(url: str) -> bool:
    import aiohttp

    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as response:
            content_type = response.headers.get('Content-Type')
            return content_type.startswith('image/')


async def validate_is_link(text: str) -> bool:
    import re
    import aiohttp

    match = re.search('(http|https)://[^\s]+', text)
    if not match:
        return False

    url = match.group()
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as response:
            return 200 <= response.status < 300
