from django.utils.translation import gettext as _
from telegram import Update
from telegram.ext import CallbackContext

from apps.tgbot.handlers.utils.decorators import get_user
from apps.tgbot.handlers.utils.states import state
from apps.users.choices import UserRoles
from apps.users.models import User


@get_user
def command_start(update: Update, context: CallbackContext, user: User):
    if not user:
        update.message.reply_text(
            text=str(_("Assalomu alaykum\nIltimos, ismingizni kiriting")),
        )
        return state.FULL_NAME

    if user.role == UserRoles.AGENCY_OPERATOR:
        update.message.reply_text(
            text=str(_("Assalomu alaykum\nXush kelibsiz!")),
        )
        return state.END

    update.message.reply_text(
        text=str(_("Assalomu alaykum\nXush kelibsiz!")),
    )
    return state.END
