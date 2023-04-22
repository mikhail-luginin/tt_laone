import os

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_API_KEY = os.environ.get('TELEGRAM_API_KEY')
WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')
EXCHANGE_COURSES_API_KEY = os.environ.get('EXCHANGE_COURSES_API_KEY')

CURRENT_WEATHER_API_CALL = (
        'http://api.openweathermap.org/data/2.5/weather?'
        'q={cityname}&'
        'appid=' + WEATHER_API_KEY + '&units=metric'
)
