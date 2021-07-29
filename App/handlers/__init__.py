from aiogram import Dispatcher

from .start import start_message
from .help import help_message
from .notifications import rbc_notify, kremlin_notify
from .send_news import rbc_news_message, kremlin_news_message


def register_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.register_message_handler(start_message, commands="start")
    dispatcher.register_message_handler(help_message, commands="help")
    dispatcher.register_message_handler(rbc_news_message, commands="rbc")
    dispatcher.register_message_handler(kremlin_news_message, commands="kremlin")
    dispatcher.register_message_handler(rbc_notify, commands="notify_rbc")
    dispatcher.register_message_handler(kremlin_notify, commands="notify_kremlin")