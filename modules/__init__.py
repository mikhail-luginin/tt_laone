from aiogram import Dispatcher


def register_all_handlers(dispatcher: Dispatcher) -> None:
    from .weather.handlers import register_weather_handlers
    from .random_images.handlers import register_random_images_handlers
    from .currency_converter.handlers import register_currency_converter_handlers
    from .admin.handlers import register_admin_handlers

    handlers = [
        register_weather_handlers,
        register_random_images_handlers,
        register_currency_converter_handlers,
        register_admin_handlers
    ]

    for handler in handlers:
        handler(dispatcher)
