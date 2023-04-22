import json
import aiohttp

import config


async def get_temperature_of_city(city_name: str) -> dict:
    url = config.CURRENT_WEATHER_API_CALL.format(cityname=city_name)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            json_data = json.loads(await response.text())

            return json_data
