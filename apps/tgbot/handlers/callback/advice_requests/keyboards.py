from django.utils.translation import gettext as _
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from apps.applications.choices import AdvisorApplicationStatus


def get_advice_requests_status_buttons(advice_request):
    def generate_callback_data(status):
        return f"advice_requests_status|{advice_request.id}|{status}"

    buttons = [
        [
            InlineKeyboardButton(
                text=str(_("📥 New")),
                callback_data=generate_callback_data(AdvisorApplicationStatus.NEW),
            ),
        ],
        [
            InlineKeyboardButton(
                text=str(_("❌ Not interested")),
                callback_data=generate_callback_data(AdvisorApplicationStatus.NOT_INTERESTED),
            ),
            InlineKeyboardButton(
                text=str(_("✅ Talked")),
                callback_data=generate_callback_data(AdvisorApplicationStatus.TALKED),
            ),
        ],
    ]

    return InlineKeyboardMarkup(buttons)
