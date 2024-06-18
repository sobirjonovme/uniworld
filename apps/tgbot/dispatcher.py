"""
    Telegram event handlers
"""
import os
from queue import Queue

from django.conf import settings
from telegram import Bot
from telegram.ext import (CallbackQueryHandler, CommandHandler,
                          ConversationHandler, Dispatcher, Filters,
                          MessageHandler, PicklePersistence)

from apps.tgbot.handlers.callback.handlers import common_callback_query_handler
from apps.tgbot.handlers.common.handlers import command_start
from apps.tgbot.handlers.eligibility_check.handlers import (
    get_age, get_certificate, get_current_education_level, get_gpa, get_name,
    get_needed_education_level, get_needed_program, get_phone_number)
from apps.tgbot.handlers.utils.states import state


def setup_dispatcher(token):
    """
    Adding handlers for events from Telegram
    """

    bot = Bot(token)
    queue = Queue()
    n_workers = 4
    if not os.path.exists(os.path.join(settings.BASE_DIR, "media")):
        os.makedirs(os.path.join(settings.BASE_DIR, "media"))

    if not os.path.exists(os.path.join(settings.BASE_DIR, "media", "state_record")):
        os.makedirs(os.path.join(settings.BASE_DIR, "media", "state_record"))

    persistence = PicklePersistence(
        filename=os.path.join(
            settings.BASE_DIR,
            "media",
            "state_record",
            "conversationbot"
            # settings.BASE_DIR, "media", "conversationbot"
        )
    )

    entry_points = [
        CommandHandler("start", command_start),
    ]
    states = {
        state.FULL_NAME: [MessageHandler(Filters.text, get_name)],
        state.PHONE_NUMBER: [MessageHandler(Filters.text, get_phone_number)],
        state.AGE: [MessageHandler(Filters.text, get_age)],
        state.CURRENT_EDUCATION_LEVEL: [
            CallbackQueryHandler(get_current_education_level),
        ],
        state.NEEDED_EDUCATION_LEVEL: [
            CallbackQueryHandler(get_needed_education_level),
        ],
        state.NEEDED_PROGRAM: [
            MessageHandler(Filters.text, get_needed_program),
        ],
        state.GPA: [
            MessageHandler(Filters.text, get_gpa),
        ],
        state.CERTIFICATE: [
            MessageHandler(Filters.text, get_certificate),
        ],
    }
    fallbacks = [
        CommandHandler("start", command_start),
    ]
    conversation_handler = ConversationHandler(
        entry_points=entry_points,
        states=states,
        fallbacks=fallbacks,
        name="conversation_handler",
        persistent=True,
        allow_reentry=True,
    )

    dp = Dispatcher(
        bot,
        update_queue=queue,
        workers=n_workers,
        use_context=True,
        persistence=persistence,
    )

    # dp.add_handler(CommandHandler("start", command_start))
    dp.add_handler(conversation_handler)
    dp.add_handler(CallbackQueryHandler(common_callback_query_handler))
    return dp
