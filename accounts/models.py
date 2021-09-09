from django.contrib.auth.models import User
from django.db import models


class Publisher(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='Publisher'
                                )
    title = models.TextField(max_length=30)
    head = models.TextField(max_length=30)

    def __str__(self):
        return f'username: {self.user.username},' \
            f'title: {self.title},' \
            f'head: {self.head}'