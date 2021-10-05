from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message

from ..services import db_add_user
from ..load_config import START_TEXT


async def start_message(message: Message) -> None:
    await db_add_user(message.from_user.id)

    await message.reply(START_TEXT, reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("/help")))
