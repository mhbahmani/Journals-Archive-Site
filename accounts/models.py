from django.contrib.auth.models import User
from django.db import models


class Publisher(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='publisher'
                                )
    title = models.TextField(max_length=30)
    head = models.TextField(max_length=30)

    def __str__(self):
        return self.title
