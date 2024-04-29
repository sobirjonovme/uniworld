from django.utils.translation import gettext as _
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from apps.applications.choices import ApplicationStatus


def get_applications_status_buttons(application):
    buttons = [
        [
            InlineKeyboardButton(
                text=str(_("📥 Received")),
                callback_data=f"applications_status|{application.id}|{ApplicationStatus.RECEIVED}",
            ),
            InlineKeyboardButton(
                text=str(_("⏳ In process")),
                callback_data=f"applications_status|{application.id}|{ApplicationStatus.IN_PROGRESS}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=str(_("❌ Cancelled")),
                callback_data=f"applications_status|{application.id}|{ApplicationStatus.CANCELLED}",
            ),
            InlineKeyboardButton(
                text=str(_("✅ Finished")),
                callback_data=f"applications_status|{application.id}|{ApplicationStatus.FINISHED}",
            ),
        ],
    ]

    return InlineKeyboardMarkup(buttons)
