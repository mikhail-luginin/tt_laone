from aiogram.dispatcher.filters.state import StatesGroup, State


class AddAdminState(StatesGroup):
    add_admin = State()


class AddPhotoState(StatesGroup):
    add_photo = State()


class PollCreatingState(StatesGroup):
    question = State()
    is_anonymous = State()
    options = State()
    explantation = State()
    poll_type = State()
