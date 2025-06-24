from django.utils.translation import gettext as _
from telegram import ParseMode

from apps.users.choices import UserRoles
from apps.applications.choices import ApplicationStatus
from apps.tgbot.handlers.callback.applications.keyboards import \
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

    operator = application.operator
    owners = application.agency.users.filter(role=UserRoles.AGENCY_OWNER)
    message_receivers = list(owners)
    message_receivers.append(operator)

    message = generate_application_info_message(application)
    buttons = get_applications_status_buttons(application)

    for receiver in message_receivers:
        if not receiver or not receiver.telegram_id:
            continue
        try:
            bot.send_message(
                chat_id=receiver.telegram_id,
                text=message,
                reply_markup=buttons,
                parse_mode=ParseMode.HTML,
            )
        except Exception as e:
            # TODO: log exception
            # STOP execution of the function if an error occurred
            print(e)
            continue

        application.sent_telegram = True
        application.save(update_fields=["sent_telegram", "updated_at"])
