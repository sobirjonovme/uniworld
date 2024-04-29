"""
    Telegram event handlers
"""
from queue import Queue

from telegram import Bot
from telegram.ext import CallbackQueryHandler, CommandHandler, Dispatcher

from apps.tgbot.handlers.callback.handlers import common_callback_query_handler
from apps.tgbot.handlers.common.handlers import command_start


def setup_dispatcher(token):
    """
    Adding handlers for events from Telegram
    """

    bot = Bot(token)
    queue = Queue()
    n_workers = 4

    dp = Dispatcher(
        bot,
        update_queue=queue,
        workers=n_workers,
        use_context=True,
    )

    dp.add_handler(CommandHandler("start", command_start))
    dp.add_handler(CallbackQueryHandler(common_callback_query_handler))
    return dp
