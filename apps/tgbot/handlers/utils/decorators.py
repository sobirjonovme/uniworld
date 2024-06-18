from functools import wraps
from typing import Callable

from telegram import ChatAction, Update
from telegram.ext import CallbackContext

from apps.users.models import User


def admin_only(func: Callable):
    """
    Admin only decorator
    Used for handlers that only admins have access to
    """

    @wraps(func)
    def wrapper(update: Update, context: CallbackContext, *args, **kwargs):
        effective_user = update.effective_user
        if not effective_user or effective_user.is_bot:
            return None

        user = User.objects.filter(telegram_id=effective_user.id).first()

        if not user or not user.is_admin:
            return

        return func(update, context, *args, **kwargs)

    return wrapper


def send_typing_action(func: Callable):
    """Sends typing action while processing func command."""

    @wraps(func)
    def command_func(update: Update, context: CallbackContext, *args, **kwargs):
        update.effective_chat.send_chat_action(ChatAction.TYPING)
        return func(update, context, *args, **kwargs)

    return command_func


def get_user(func):
    def wrap(update, context, *args, **kwargs):
        effective_user = update.effective_user
        if not effective_user or effective_user.is_bot:
            return None

        user = User.objects.filter(telegram_id=effective_user.id).first()
        # if not user:
        #     txt = "You cannot use this bot. It is not for public use!"
        #     try:
        #         context.bot.send_message(chat_id=effective_user.id, text=txt)
        #     except Exception:
        #         pass
        #     return None

        return func(update, context, user, *args, **kwargs)

    return wrap
