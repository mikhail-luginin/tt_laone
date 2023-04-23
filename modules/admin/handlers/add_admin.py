from aiogram import types
from aiogram.dispatcher import FSMContext

from .. import validators, states
from .. decorators import check_admin


@check_admin
async def add_admin_command_handler(message: types.Message):
    """
    This handler called after command /add_admin and used for start AddAdminState.

    :param message:
    :type message: types.Message

    :return:
    """

    sender_username = message.from_user.username

    is_admin = await validators.validate_is_admin(sender_username)

    if is_admin:
        await message.answer(text='Enter username for add to admin list '
                                  '(without @, for example: PetrPetrov, IvanIvanov)')
        await states.AddAdminState.add_admin.set()


async def add_admin_state_handler(message: types.Message, state: FSMContext):
    """
    This handler used for add admin to admins list.

    :param message:
    :type message: types.Message

    :param state:
    :type state: FSMContext

    :return:
    """

    username_to_add = message.text.strip()

    with open('modules/admin/admins.txt', 'a') as file:
        file.write('\n' + username_to_add)

    success_message = f"Administrator {username_to_add} was successfully added to the list!"
    await message.answer(text=success_message)

    await state.finish()
