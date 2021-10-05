from aiogram import Dispatcher
from aiogram.types import BotCommand


async def set_bot_commands(dp: Dispatcher):
    await dp.bot.set_my_commands([
        BotCommand("start", "Приветственное сообщение"),
        BotCommand("help", "Помощь"),
        BotCommand("rbc", "Новости с сайта rbc.ru"),
        BotCommand("kremlin", "Новости с сайта kremlin.ru"),
        BotCommand("lenta", "Новости с сайта lenta.ru"),
        BotCommand("notify_rbc", "Настройка уведомлений о новостях на rbc.ru"),
        BotCommand("notify_kremlin", "Настройка уведомлений о новостях на kremlin.ru"),
        BotCommand("notify_lenta", "Настройка уведомлений о новостях на lenta.ru")
    ])
