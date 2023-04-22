from .api import get_temperature_of_city


async def get_temperature(city_name: str) -> str:
    json_data = await get_temperature_of_city(city_name)

    if 'cod' in json_data and json_data['cod'] == '404':
        return 'City not found :('

    city = json_data['name']
    temperature = round(json_data['main']['temp'])
    return f'City: {city}\n\nCurrent temperature: {temperature}°C'
