from django.utils.translation import gettext as _
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup,
                      KeyboardButton, ReplyKeyboardMarkup)

from apps.applications.choices import (CurrentEducationLevelChoices,
                                       NeededEducationLevelChoices)
from apps.universities.models import Specialty


def get_current_education_level_buttons():
    def generate_callback_data(status):
        return f"current_education_level|{status}"

    buttons = [
        [
            InlineKeyboardButton(
                text=str(_("Maktab bitiruvchisi")),
                callback_data=generate_callback_data(CurrentEducationLevelChoices.HIGH_SCHOOL),
            ),
        ],
        [
            InlineKeyboardButton(
                text=str(_("Bakalavr")),
                callback_data=generate_callback_data(CurrentEducationLevelChoices.BACHELOR),
            ),
        ],
    ]

    return InlineKeyboardMarkup(buttons)


def get_needed_education_level_buttons():
    def generate_callback_data(status):
        return f"needed_education_level|{status}"

    buttons = [
        [
            InlineKeyboardButton(
                text=str(_("Bakalavr")),
                callback_data=generate_callback_data(NeededEducationLevelChoices.BACHELOR),
            ),
        ],
        [
            InlineKeyboardButton(
                text=str(_("Magistr")),
                callback_data=generate_callback_data(NeededEducationLevelChoices.MASTER),
            ),
        ],
    ]

    return InlineKeyboardMarkup(buttons)


def get_needed_program_keyboard():
    specialties = Specialty.objects.all().order_by("name")
    specialties_count = specialties.count()
    buttons = []

    for index, specialty in enumerate(specialties):
        if index % 2 == 0:
            buttons.append([])
        buttons[-1].append(KeyboardButton(text=specialty.name))

    if specialties_count % 2 == 0:
        buttons.append([KeyboardButton(text="Boshqa")])
    else:
        buttons[-1].append(KeyboardButton(text="Boshqa"))

    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)
