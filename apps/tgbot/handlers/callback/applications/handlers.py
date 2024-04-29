from django.utils.translation import gettext as _
from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from apps.applications.models import Application
from apps.tgbot.services.applications import generate_application_info_message
from apps.users.models import User

from .keyboards import get_applications_status_buttons


# NO need to add get_user decorator here, because it's already added in the common_callback_query_handler
def get_application_status(update: Update, context: CallbackContext, user: User):

    data = update.callback_query.data
    data_list = data.split("|")

    application = Application.objects.filter(id=data_list[1]).first()
    if application:
        application.status = data_list[2]
        application.save(update_fields=["status", "updated_at"])
        update.callback_query.answer(text=str(_("Application status changed successfully!")))

        buttons = get_applications_status_buttons(application)
        txt = generate_application_info_message(application)
        update.callback_query.edit_message_text(
            text=txt,
            reply_markup=buttons,
            parse_mode=ParseMode.HTML,
        )

        return
