import re

from bot.models import TelegramUser, Message, Category, Expense


def greet_and_save_user_message(user_id, message_text, message_id):
    user, created = TelegramUser.objects.get_or_create(telegram_id=user_id)
    name = user.name

    answer_text = ''

    if created:
        answer_text += 'Видимся впервые. '

    if name:
        answer_text += f'Привет, {name}.'
    else:
        answer_text += 'Мы еще не знакомы. ID текущего чата =' + str(user_id)
        answer_text += ' А как вас зовут? напишите командой /set_name'

    message = Message(
        user=user,
        text=message_text,
        telegram_id=message_id,
    )
    message.save()

    return answer_text


def set_user_name(user_id, name):
    user, _ = TelegramUser.objects.get_or_create(telegram_id=user_id)
    user.name = name
    user.save()


def set_expense(user_id, category_title, amount):
    user, _ = TelegramUser.objects.get_or_create(telegram_id=user_id)
    category, _ = Category.objects.get_or_create(title=category_title)
    expense = Expense(user=user, category=category, amount=amount)
    expense.save()


def get_expenses_text(expenses):
    expenses_text = ''
    total = 0

    for e in expenses:
        expenses_text += str(e.amount) + ' потратили на ' + e.category.title
        expenses_text += '\n'
        total += e.amount

    return expenses_text + '\n\n' + f'Общее кол-во затрат: {total}'


def show_all_expenses(user_id):

    user, _ = TelegramUser.objects.get_or_create(telegram_id=user_id)

    expenses = Expense.objects.filter(user=user)
    return get_expenses_text(expenses)


def show_expenses_of_category(user_id, category_title):

    user, _ = TelegramUser.objects.get_or_create(telegram_id=user_id)
    try:
        category = Category.objects.get(title=category_title)
    except Category.DoesNotExist:
        return 'Такой категории нет'

    expenses = Expense.objects.filter(user=user, category=category)
    return get_expenses_text(expenses)
