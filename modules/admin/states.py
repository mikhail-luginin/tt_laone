from aiogram.dispatcher.filters.state import StatesGroup, State


class AddAdminState(StatesGroup):
    add_admin = State()


class AddPhotoState(StatesGroup):
    add_photo = State()


class PollCreatingState(StatesGroup):
    chat_id = State()
    question = State()
    is_anonymous = State()
    options = State()
    poll_type = State()
    correct_option = State()
