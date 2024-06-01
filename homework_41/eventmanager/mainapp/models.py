from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"
        verbose_name_plural = "category"


class Event(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    date = models.DateField()
    location = models.CharField(max_length=50)
    category = models.ManyToManyField(Category)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "event"
        verbose_name_plural = "event"
