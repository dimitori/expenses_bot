# Generated by Django 3.1.3 on 2020-12-06 17:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_auto_20201115_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='date_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='telegram_id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Id of telegram user'),
        ),
    ]