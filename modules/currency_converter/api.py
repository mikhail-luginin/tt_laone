import aiohttp
import json
import config


async def currency_converter(current_currency: str, currency_for_convert: str, amount: int) -> str:
    url = config.CURRENT_EXCHANGE_COURSES_API_CALL.format(current_currency=current_currency,
                                                          currency_for_convert=currency_for_convert,
                                                          amount=amount)
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=config.CURRENT_EXCHANGE_COURSES_API_HEADERS, ssl=False) as response:
            try:
                json_data = await response.json()
            except json.JSONDecodeError:
                raise ValueError('Invalid JSON response')

            if json_data.get('error') is not None:
                if json_data['error']['code'] == 'invalid_from_currency':
                    raise ValueError('Current currency is invalid')
                elif json_data['error']['code'] == 'invalid_to_currency':
                    raise ValueError('Currency for convert is invalid')

            if json_data['success']:
                result = json_data["result"]
                result_str = f'Your current currency: {current_currency}\n' \
                             f'Currency for convert: {currency_for_convert}\n' \
                             f'Amount: {amount}\n\n' \
                             f'Result: {round(result)} (result was rounded, not rounded result: {result})'
                return result_str.strip()
