from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message

from services import db_add_user
from load_config import HELP_TEXT

async def help_message(message: Message) -> None:
    await db_add_user(message.from_user.id)
    
    rbc_button = KeyboardButton("/rbc")
    kremlin_button = KeyboardButton("/kremlin")
    notify_rbc_btn = KeyboardButton("/notify_rbc")
    notify_kremlin_btn = KeyboardButton("/notify_kremlin")
    
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(rbc_button, kremlin_button, notify_rbc_btn, notify_kremlin_btn)

    await message.reply(HELP_TEXT, reply_markup=keyboard)