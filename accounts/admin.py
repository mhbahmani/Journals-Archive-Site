from django.contrib import admin
from accounts.models import Publisher


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass
