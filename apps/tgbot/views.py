import json
import logging

from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views import View
from telegram import Update

from apps.tgbot.dispatcher import setup_dispatcher
from apps.tgbot.main import bot

logger = logging.getLogger(__name__)


# @app.task(ignore_result=True)
def process_telegram_event(update_json):
    token = settings.BOT_TOKEN
    dispatcher = setup_dispatcher(token)

    update = Update.de_json(update_json, bot)
    dispatcher.process_update(update)


class TelegramBotWebhookView(View):
    # WARNING: if fail - Telegram webhook will be delivered again.
    # Can be fixed with async celery task execution
    def post(self, request, *args, **kwargs):
        bot_secret_key = request.headers.get("X-Telegram-Bot-Api-Secret-Token")
        if bot_secret_key != settings.BOT_SECRET_KEY:
            return HttpResponse(status=400)

        # if settings.RUN_BOT_CELERY:
        #     # Process Telegram event in Celery worker (async)
        #     # Don't forget to run it and & Redis (message broker for Celery)!
        #     # Locally, You can run all of these services via docker-compose.yml
        #     process_telegram_event.delay(json.loads(request.body))
        # else:
        process_telegram_event(json.loads(request.body))

        # e.g. remove buttons, typing event
        return JsonResponse({"ok": "POST request processed"})

    def get(self, request, *args, **kwargs):  # for debug
        return JsonResponse({"ok": "Get request received! But nothing done"})
