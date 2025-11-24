from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField("Название")
    text = models.TextField("Текст")
    deadline = models.DateTimeField("Дедлайн")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title

