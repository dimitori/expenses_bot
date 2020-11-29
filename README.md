# razrabotka expense BOT

Чтобы проект работал:
- создать виртуальное окружение (`python3 -m venv venv`)
- включить его (`source venv/bin/activate`)
- установить зависимости (`pip install -r requirements.txt`)

Для запуска бота нужно:
- взять своего бота (или зарегать в BotFather) и добавить ему команды из списка ниже;
- добавить переменную окружения (export TG_TOKEN='токен');
стоит хранить переменные окружения в файле .env
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
