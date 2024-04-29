from telegram import Update
from telegram.ext import CallbackContext

from apps.tgbot.handlers.callback.advice_requests.handlers import \
    get_advice_request_status
from apps.tgbot.handlers.callback.applications.handlers import \
    get_application_status
from apps.tgbot.handlers.utils.decorators import get_user
from apps.users.models import User


@get_user
def common_callback_query_handler(update: Update, context: CallbackContext, user: User):
    data = update.callback_query.data
    data_list = data.split("|")

    if data_list[0] == "applications_status":
        get_application_status(update, context, user)
        return
    elif data_list[0] == "advice_requests_status":
        get_advice_request_status(update, context, user)
        return

    update.callback_query.answer()
