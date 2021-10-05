from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from ..services import db_add_user, db_update_user
from ..load_config import ON_RBC_TEXT, OFF_RBC_TEXT


async def rbc_notify(message) -> None:
    await db_add_user(message.from_user.id)
    is_notifications_on = await db_update_user(message.from_user.id, "rbc")

    if is_notifications_on is True:
        await message.reply(ON_RBC_TEXT, reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("/help")))
    
    if is_notifications_on is False:
        await message.reply(OFF_RBC_TEXT, reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("/help")))