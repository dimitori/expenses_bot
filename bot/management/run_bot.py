from django.core.management.base import BaseCommand
from bot.bot import run_bot


class Command(BaseCommand):
    help = 'Telegram-bot'

    def handle(self, *args, **options):
        run_bot()
