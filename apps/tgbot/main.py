from django.conf import settings
from telegram import Bot

try:
    bot = Bot(settings.BOT_TOKEN)
    TELEGRAM_BOT_USERNAME = bot.get_me()["username"]
except:  # noqa E722
    bot = None
