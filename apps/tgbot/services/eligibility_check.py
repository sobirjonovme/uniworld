import typing

from django.utils.translation import gettext as _
from telegram import ParseMode

from apps.applications.choices import (CurrentEducationLevelChoices,
                                       NeededEducationLevelChoices)
from apps.common.models import SiteSettings
from apps.tgbot.main import bot


def generate_eligibility_check_application_message(user_data: typing.Dict) -> str:
    current_education_level = user_data.get("current_education_level")
    current_education = dict(CurrentEducationLevelChoices.choices).get(current_education_level)
    needed_education_level = user_data.get("needed_education_level")
    needed_education = dict(NeededEducationLevelChoices.choices).get(needed_education_level)
    program = user_data.get("program")
    phone_number = user_data.get("phone_number")

    username = user_data.get("username")
    if username:
        username = f"@{username}"
    else:
        username = f"t.me/{phone_number}"

    msg = str(
        _(
            "<b><i>📑 Eligibility Checking</i></b>\n\n"
            "<i>Ismi</i>: <b>{full_name}</b>\n"
            "<i>Bog'lanish</i>: <b>{username}</b>\n"
            "<i>Telefon raqami</i>: <b>{phone_number}</b>\n"
            "<i>Yoshi</i>: <b>{age}</b>\n"
            "<i>Hozirgi ta'lim darajasi</i>: <b>{current_education_level}</b>\n"
            "<i>O'qimoqchi</i>: <b>{needed_education_level}</b>\n"
            "<i>Ta'lim yo'nalishi</i>: <b>{program}</b>\n"
            "<i>GPA</i>: <b>{gpa}</b>\n"
            "<i>Sertifikatlar</i>: <b>{certificate}</b>\n"
        )
    ).format(
        full_name=user_data.get("full_name"),
        username=username,
        phone_number=user_data.get("phone_number"),
        age=user_data.get("age"),
        current_education_level=current_education,
        needed_education_level=needed_education,
        program=program,
        gpa=user_data.get("gpa"),
        certificate=user_data.get("certificate"),
    )

    return msg


def send_eligibility_check_application_message_to_group(user_data):
    site_settings = SiteSettings.get_solo()
    chat_id = site_settings.advice_requests_chat_id

    if bot is None or not chat_id:
        return

    # send message to group
    msg = generate_eligibility_check_application_message(user_data)
    try:
        bot.send_message(
            chat_id=chat_id,
            text=msg,
            parse_mode=ParseMode.HTML,
        )
    except Exception:
        # TODO: log exception
        # STOP execution of the function if an error occurred
        return
