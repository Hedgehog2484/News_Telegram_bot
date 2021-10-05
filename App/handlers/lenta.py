from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message

from ..services import db_add_user, parse_lenta


async def lenta_news_message(message: Message) -> None:
    await db_add_user(message.from_user.id)

    count = 0
    message_text = "Последние новости с сайта lenta.ru:\n\n"

    news = await parse_lenta()
    for j in news:
        count += 1
        message_text += f"{count}. [{j}]({news[j]})\n\n"

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("/help"))
    await message.reply(message_text, reply_markup=keyboard, parse_mode='Markdown', disable_web_page_preview=True)
