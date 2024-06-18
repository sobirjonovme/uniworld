from django.utils.translation import gettext as _
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import CallbackContext

from apps.tgbot.handlers.utils.decorators import get_user
from apps.tgbot.handlers.utils.states import state
from apps.tgbot.services.eligibility_check import \
    send_eligibility_check_application_message_to_group
from apps.users.models import User

from .keyboards import (get_current_education_level_buttons,
                        get_needed_education_level_buttons,
                        get_needed_program_keyboard)


@get_user
def get_name(update: Update, context: CallbackContext, user: User):
    full_name = update.message.text
    context.user_data["full_name"] = full_name

    msg = str(_("Telefon raqamingizni kiriting:\n\n" "<i>(Masalan, <code>+998907071122</code>)</i>"))
    update.message.reply_text(msg, parse_mode="HTML")

    return state.PHONE_NUMBER


@get_user
def get_phone_number(update: Update, context: CallbackContext, user: User):
    phone_number_str = update.message.text
    phone_number = "+"
    for char in phone_number_str:
        if char.isdigit():
            phone_number += char

    context.user_data["phone_number"] = phone_number

    msg = str(_("Iltimos, yoshingizni kiriting:"))
    update.message.reply_text(msg, parse_mode="HTML")

    return state.AGE


@get_user
def get_age(update: Update, context: CallbackContext, user: User):
    age = update.message.text

    # check if age is a number
    if not age.isdigit():
        msg = str(_("Iltimos, yoshingizni raqamda kiriting:"))
        update.message.reply_text(msg, parse_mode="HTML")
        return state.AGE

    context.user_data["age"] = age

    msg = str(_("Hozirgi ta'lim darajangizni tanlang:"))
    buttons = get_current_education_level_buttons()
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=msg,
        reply_markup=buttons,
        parse_mode="HTML",
    )

    return state.CURRENT_EDUCATION_LEVEL


@get_user
def get_current_education_level(update: Update, context: CallbackContext, user: User):
    query = update.callback_query
    query.answer()

    data_list = query.data.split("|")
    current_education_level = data_list[1]
    context.user_data["current_education_level"] = current_education_level

    msg = str(_("Qaysi o'quv daraja bo'yicha o'qimoqchisiz?"))
    buttons = get_needed_education_level_buttons()
    # edit old message
    query.edit_message_text(text=msg, reply_markup=buttons, parse_mode="HTML")

    return state.NEEDED_EDUCATION_LEVEL


@get_user
def get_needed_education_level(update: Update, context: CallbackContext, user: User):
    query = update.callback_query
    query.answer()

    data_list = query.data.split("|")
    needed_education_level = data_list[1]
    context.user_data["needed_education_level"] = needed_education_level

    msg = str(_("Qaysi yo'nalishda o'qimoqchisiz?"))
    keyboard = get_needed_program_keyboard()
    query.delete_message()
    context.bot.send_message(
        chat_id=query.message.chat_id,
        text=msg,
        reply_markup=keyboard,
        parse_mode="HTML",
    )

    return state.NEEDED_PROGRAM


@get_user
def get_needed_program(update: Update, context: CallbackContext, user: User):
    program = update.message.text
    context.user_data["program"] = program

    msg = str(
        _(
            "GPA ko'rsatkichingizni kiriting:\n"
            "Masalan, <code>4.6/5</code>\n\n"
            "<i>(Atestatdagi fanlar baholarini bir-biriga qo'shib, "
            "ularning yig'indisini fanlarning umumiy soniga bo'lganda kelib chiqadi)</i>"
        )
    )
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=msg,
        parse_mode="HTML",
        reply_markup=ReplyKeyboardRemove(),
    )

    return state.GPA


@get_user
def get_gpa(update: Update, context: CallbackContext, user: User):
    gpa = update.message.text
    context.user_data["gpa"] = gpa

    msg = str(
        _(
            "Sizda quyidagi sertifikatlar bormi? <i>(IELTS, TOEFL, SAT, GMAT)</i>\n"
            "Agar bo'lsa, ularni kiriting, aks holda <code>Yo'q</code> deb yozing.\n\n"
            "Masalan, <code>IELTS 6.5, TOEFL 100</code>."
        )
    )
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=msg,
        parse_mode="HTML",
    )

    return state.CERTIFICATE


@get_user
def get_certificate(update: Update, context: CallbackContext, user: User):
    certificate = update.message.text
    context.user_data["certificate"] = certificate

    data = context.user_data
    data["username"] = update.effective_user.username

    send_eligibility_check_application_message_to_group(user_data=data)

    msg = str(_("Rahmat! Sizning ma'lumotlaringiz qabul qilindi."))
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=msg,
        parse_mode="HTML",
    )

    return state.END
