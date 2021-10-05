from aiogram import Dispatcher

from .start import start_message
from .help import help_message
from .rbc import rbc_news_message
from .kremlin import kremlin_news_message
from .lenta import lenta_news_message
from .notifications_rbc import rbc_notify
from .notifications_kremlin import kremlin_notify
from .notifications_lenta import lenta_notify


def register_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.register_message_handler(start_message, commands="start")
    dispatcher.register_message_handler(help_message, commands="help")
    dispatcher.register_message_handler(rbc_news_message, commands="rbc")
    dispatcher.register_message_handler(kremlin_news_message, commands="kremlin")
    dispatcher.register_message_handler(lenta_news_message, commands="lenta")
    dispatcher.register_message_handler(rbc_notify, commands="notify_rbc")
    dispatcher.register_message_handler(kremlin_notify, commands="notify_kremlin")
    dispatcher.register_message_handler(lenta_notify, commands="notify_lenta")
