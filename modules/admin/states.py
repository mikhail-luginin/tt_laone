from aiogram.dispatcher.filters.state import StatesGroup, State


class AddAdminState(StatesGroup):
    add_admin = State()


class AddPhotoState(StatesGroup):
    add_photo = State()
