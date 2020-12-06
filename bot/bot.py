from bot.services.bot_service import (
    greet_and_save_user_message,
    set_user_name,
    set_expense,
    show_all_expenses,
    show_expenses_of_category,
)

from django.conf import settings
from telegram.ext import Updater, CommandHandler, \
    MessageHandler, Filters
from telegram import Bot
from telegram.utils.request import Request
import re


request = Request(
    connect_timeout=0.5,
    read_timeout=1.0,
)
bot = Bot(
    request=request,
    token=settings.TG_TOKEN,
    base_url=settings.PROXY_URL,
)
connected = False

updater = Updater(
    bot=bot,
    use_context=True
)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def set_name(update, context):
    name = ' '.join(context.args)
    # получили имя
    # должны записать его в базу данных
    # записываем имя именно пользователю с этим chat_id
    set_user_name(update.effective_user.id, name)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Имя задано: {name}"
    )


def expense(update, context):
    args = context.args

    try:
        category_title = args[0]
        amount = float(args[1])

        set_expense(update.effective_user.id, category_title, amount)

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Трата записана: {category_title} - {amount} рублей"
        )

    except IndexError:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Не хватает параметров. нужно указать категорию и сумму"
        )


def show_expenses(update, context):
    args = context.args

    try:
        category_title = args[0]
        expenses_text = show_expenses_of_category(update.effective_user.id, category_title)

    except IndexError:
        expenses_text = show_all_expenses(update.effective_user.id)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=expenses_text,
    )


def greeting(update, context):

    user_id = update.effective_user.id
    message = update.effective_message

    answer_text = greet_and_save_user_message(
        user_id,
        message.text,
        message.message_id,
    )

    context.bot.send_message(
        chat_id=user_id,
        text=answer_text,
    )


def run_bot():
    start_handler = CommandHandler('start', start)
    set_name_handler = CommandHandler('set_name', set_name)
    expense_handler = CommandHandler('expense', expense)
    show_expenses_handler = CommandHandler('show_expenses', show_expenses)

    # work_handler = MessageHandler(Filters.regex(r"сегодня\s+я\s+поработал\s+(\d+)\s+ч") & (~Filters.command), set_work)
    greeting_handler = MessageHandler(Filters.text & (~Filters.command), greeting)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(set_name_handler)
    updater.dispatcher.add_handler(expense_handler)
    updater.dispatcher.add_handler(show_expenses_handler)

    updater.dispatcher.add_handler(greeting_handler)

    updater.start_polling()
    print('Бот запущен')
    updater.idle()


if __name__ == '__main__':
    run_bot()
