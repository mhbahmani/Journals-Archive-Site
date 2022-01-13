from django.db import models

from accounts.models import Publisher


class Publication(models.Model):
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='publications/')
    show = models.BooleanField(default=True)

    def get_image_name(self):
        return self.pdf.name[12:-4]

    def get_title(self):
        return self.title[0:10] + '...'

    class Meta:
        ordering = ['-id']
     
    def __str__(self):
        return f"{self.title}"


