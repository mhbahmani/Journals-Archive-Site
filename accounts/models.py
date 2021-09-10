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
        return f'username: {self.user.username},' \
            f'title: {self.title},' \
            f'head: {self.head}'


class Publication(models.Model):
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    title = models.CharField(max_length = 80)
    pdf = models.FileField(upload_to='publications/')
 
    class Meta:
        ordering = ['title']
     
    def __str__(self):
        return f"{self.title}"