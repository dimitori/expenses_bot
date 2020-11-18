# razrabotka expense BOT

Для запуска бота нужно:
- взять своего бота (или зарегать в BotFather) и добавить ему команды из списка ниже;
- вставить токен бота в конец файла settings.py (TG_TOKEN='токен');
- запустить бота командой `./manage.py run_bot`

Для запуска админки:
- `./manage.py migrate` (только в первый раз)
- `./manage.py createsuperuser` (только 1 раз создаем пользователя)
- `./manage.py runserver`

Список команд бота:

```
start - Start bot
set_name - set name
expense - add a new expense
show_expenses - show expenses
```