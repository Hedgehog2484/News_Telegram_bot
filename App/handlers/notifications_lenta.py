from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message

from ..services import db_add_user, db_update_user
from ..load_config import ON_LENTA_TEXT, OFF_LENTA_TEXT


async def lenta_notify(message: Message) -> None:
    await db_add_user(message.from_user.id)
    is_notifications_on = await db_update_user(message.from_user.id, "lenta")

    if is_notifications_on is True:
        await message.reply(ON_LENTA_TEXT, reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("/help")))

    if is_notifications_on is False:
        await message.reply(OFF_LENTA_TEXT, reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("/help")))