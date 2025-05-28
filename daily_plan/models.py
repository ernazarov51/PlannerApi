from django.db import models
from django.db.models import Model, CharField, TextChoices, ForeignKey, CASCADE, DateTimeField


# Create your models here.
class Category(Model):
    name = CharField(max_length=255)
    user = ForeignKey('authentication.User', CASCADE, related_name='categories')


class Plan(Model):
    class PriorityChoices(TextChoices):
        high = 'yuqori', 'Yuqori'  # noqa
        medium = "o'rta", "O'rta"  # noqa
        low = 'past', 'Past'

    name = CharField(max_length=255)
    priority = CharField(max_length=255, choices=PriorityChoices.choices)
    category = ForeignKey('daily_plan.Category', CASCADE, related_name='plans')
    description = CharField(max_length=500)
    deadline = DateTimeField()
    user = ForeignKey('authentication.User', CASCADE, related_name='plans')
    note=CharField(max_length=255)

