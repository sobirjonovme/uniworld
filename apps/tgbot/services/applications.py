from django.utils.translation import gettext as _
from telegram import ParseMode

from apps.applications.choices import ApplicationStatus
from apps.tgbot.handlers.applications.keyboards import \
    get_applications_status_buttons
from apps.tgbot.main import bot


def generate_application_info_message(application):
    status_texts = {
        ApplicationStatus.RECEIVED: _("📥 Received"),
        ApplicationStatus.IN_PROGRESS: _("⏳ In process"),
        ApplicationStatus.CANCELLED: _("❌ Cancelled"),
        ApplicationStatus.FINISHED: _("✅ Finished"),
    }

    txt = str(
        _(
            "<b><i>📝 Application info</i></b>\n\n"
            "<b>Status:</b>   {status}\n\n"
            "<b>Full name:</b> {full_name}\n"
            "<b>Phone number:</b> {phone_number}\n"
            "<b>University:</b> {university}\n"
            "<b>Course:</b> {course}\n"
            "<b>Age:</b> {age}\n"
            "<b>Gender:</b> {gender}\n"
        )
    ).format(
        status=status_texts[application.status],
        university=application.university.name,
        course=application.course.name if application.course else "—",
        full_name=f"{application.first_name} {application.last_name}",
        phone_number=application.phone_number,
        age=application.age,
        gender=application.get_gender_display(),
    )

    return txt


def send_application_info_to_operator(application):
    if bot is None:
        return

    if not application.operator or not application.operator.telegram_id:
        return

    message = generate_application_info_message(application)
    buttons = get_applications_status_buttons(application)

    bot.send_message(
        chat_id=application.operator.telegram_id,
        text=message,
        reply_markup=buttons,
        parse_mode=ParseMode.HTML,
    )
