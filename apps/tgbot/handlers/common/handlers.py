from django.utils.translation import gettext as _
from telegram import Update
from telegram.ext import CallbackContext

from apps.tgbot.handlers.utils.decorators import get_user
from apps.users.models import User


@get_user
def command_start(update: Update, context: CallbackContext, user: User):
    update.message.reply_text(
        text=str(_("Assalomu alaykum\nXush kelibsiz!")),
    )
