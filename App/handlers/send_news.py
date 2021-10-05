from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message

from ..services import db_add_user, parse_kremlin, parse_rbc


async def kremlin_news_message(message: Message) -> None:
    await db_add_user(message.from_user.id)

    count = 0
    message_text = "Последние новости с сайта kremlin:\n\n"

    news = await parse_kremlin()
    for j in news:
        count += 1
        message_text += f"{count}. [{j}]({news[j]})\n\n"

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("/help"))
    await message.reply(message_text, reply_markup=keyboard, parse_mode='Markdown', disable_web_page_preview = True)


async def rbc_news_message(message: Message) -> None:
    await db_add_user(message.from_user.id)

    count = 0
    message_text = "Последние новости с сайта rbc:\n\n"


    news = await parse_rbc()
    for j in news:
        count += 1
        message_text += f"{count}. [{j}]({news[j]})\n\n"

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("/help"))
    await message.reply(message_text, reply_markup=keyboard, parse_mode='Markdown', disable_web_page_preview = True)