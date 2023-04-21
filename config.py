import os

from dotenv import load_dotenv


load_dotenv()

TELEGRAM_API_KEY = os.environ.get('TELEGRAM_API_KEY')
WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')
EXCHANGE_COURSES_API_KEY = os.environ.get('EXCHANGE_COURSES_API_KEY')
