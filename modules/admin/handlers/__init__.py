from aiogram import Dispatcher

from .add_admin import add_admin_command_handler, add_admin_state_handler
from .add_photo import add_photo_command_handler, add_photo_state_handler
from .create_poll import create_poll_command_handler, poll_question_state_handler, poll_options_state_handler, \
    poll_type_state_handler, poll_is_anonymous_state_handler, poll_correct_option_state_handler, \
    poll_chat_id_state_handler

from .. import states


def register_admin_handlers(dispatcher: Dispatcher) -> None:
    message_handlers = [
        dict(callback=add_admin_command_handler, commands=['add_admin']),
        dict(callback=add_admin_state_handler, state=states.AddAdminState.add_admin),

        dict(callback=add_photo_command_handler, commands=['add_photo']),
        dict(callback=add_photo_state_handler, state=states.AddPhotoState.add_photo),

        dict(callback=create_poll_command_handler, commands=['create_poll']),
        dict(callback=poll_chat_id_state_handler, state=states.PollCreatingState.chat_id),
        dict(callback=poll_question_state_handler, state=states.PollCreatingState.question),
        dict(callback=poll_options_state_handler, state=states.PollCreatingState.options)
    ]

    callback_query_handlers = [
        dict(callback=poll_is_anonymous_state_handler, state=states.PollCreatingState.is_anonymous),
        dict(callback=poll_type_state_handler, state=states.PollCreatingState.poll_type),
        dict(callback=poll_correct_option_state_handler, state=states.PollCreatingState.correct_option)
    ]

    for handler in message_handlers:
        dispatcher.register_message_handler(**handler)

    for handler in callback_query_handlers:
        dispatcher.register_callback_query_handler(**handler)
