from django.utils.translation import gettext as _
from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from apps.applications.models import AdvisorApplication
from apps.tgbot.services.advice_requests import \
    generate_advice_request_info_message
from apps.users.models import User

from .keyboards import get_advice_requests_status_buttons


# NO need to add get_user decorator here, because it's already added in the common_callback_query_handler
def get_advice_request_status(update: Update, context: CallbackContext, user: User):

    data = update.callback_query.data
    data_list = data.split("|")

    application = AdvisorApplication.objects.filter(id=data_list[1]).first()
    if application:
        application.status = data_list[2]
        application.save(update_fields=["status", "updated_at"])
        update.callback_query.answer(text=str(_("Advice Request Application status changed successfully!")))

        buttons = get_advice_requests_status_buttons(application)
        txt = generate_advice_request_info_message(application)
        update.callback_query.edit_message_text(
            text=txt,
            reply_markup=buttons,
            parse_mode=ParseMode.HTML,
        )

        return
