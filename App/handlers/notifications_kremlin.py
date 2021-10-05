from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from ..services import db_add_user, db_update_user
from ..load_config import ON_KREMLIN_TEXT, OFF_KREMLIN_TEXT


async def kremlin_notify(message) -> None:
    await db_add_user(message.from_user.id)
    is_notifications_on = await db_update_user(message.from_user.id, "kremlin")

    if is_notifications_on is True:
        await message.reply(ON_KREMLIN_TEXT, reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("/help")))

    if is_notifications_on is False:
        await message.reply(OFF_KREMLIN_TEXT, reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("/help")))