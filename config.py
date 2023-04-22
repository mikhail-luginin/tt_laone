import os

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_API_KEY = os.environ.get('TELEGRAM_API_KEY')
WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')
EXCHANGE_COURSES_API_KEY = os.environ.get('EXCHANGE_COURSES_API_KEY')

CURRENT_WEATHER_API_CALL = (
        'https://api.openweathermap.org/data/2.5/weather?'
        'q={cityname}&'
        'appid=' + WEATHER_API_KEY + '&units=metric'
)

CURRENT_EXCHANGE_COURSES_API_CALL = (
        'https://api.apilayer.com/exchangerates_data/convert?'
        '&from={current_currency}&to={currency_for_convert}&amount={amount}'
)

CURRENT_EXCHANGE_COURSES_API_HEADERS = {
        'apikey': EXCHANGE_COURSES_API_KEY
}
