from django.db import models


class TelegramUser(models.Model):
    telegram_id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.telegram_id}-{self.name}"


class Message(models.Model):
    user = models.ForeignKey(to=TelegramUser, on_delete=models.CASCADE)
    text = models.TextField()
    telegram_id = models.IntegerField()

    def __str__(self):
        return f"{self.user}-{self.telegram_id}"


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Expense(models.Model):
    user = models.ForeignKey(to=TelegramUser, on_delete=models.CASCADE)
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True)
    amount = models.FloatField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}-{self.category}-{self.amount}"
