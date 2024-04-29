from django.utils.translation import gettext as _
from telegram import ParseMode

from apps.applications.choices import AdvisorApplicationStatus
from apps.common.models import SiteSettings
from apps.tgbot.handlers.callback.advice_requests.keyboards import \
    get_advice_requests_status_buttons
from apps.tgbot.main import bot


def generate_advice_request_info_message(advice_request):
    status_texts = {
        AdvisorApplicationStatus.NEW: _("📥 New"),
        AdvisorApplicationStatus.TALKED: _("✅ Talked"),
        AdvisorApplicationStatus.NOT_INTERESTED: _("❌ Not interested"),
    }

    txt = str(
        _(
            "<b><i>📝 Request for Advice info</i></b>\n\n"
            "<b>Status:</b>   {status}\n\n"
            "<b>Full name:</b> {full_name}\n"
            "<b>Who:</b> {who}\n"
            "<b>Phone number:</b> {phone_number}\n"
            "<b>Country:</b> {country}\n"
            "<b>Region:</b> {region}\n"
        )
    ).format(
        status=status_texts.get(advice_request.status, "—"),
        full_name=f"{advice_request.first_name} {advice_request.last_name}",
        who=advice_request.get_who_are_you_display(),
        phone_number=advice_request.phone_number,
        country=advice_request.country.name if advice_request.country else "—",
        region=advice_request.region.name if advice_request.region else "—",
    )

    return txt


def send_advice_request_info_to_operator(advice_request):
    site_settings = SiteSettings.get_solo()
    chat_id = site_settings.advice_requests_chat_id

    if bot is None or not chat_id:
        return

    message = generate_advice_request_info_message(advice_request)
    buttons = get_advice_requests_status_buttons(advice_request)

    try:
        bot.send_message(
            chat_id=chat_id,
            text=message,
            reply_markup=buttons,
            parse_mode=ParseMode.HTML,
        )
    except Exception:
        # TODO: log exception
        # STOP execution of the function if an error occurred
        return

    advice_request.sent_telegram = True
    advice_request.save(update_fields=["sent_telegram", "updated_at"])
