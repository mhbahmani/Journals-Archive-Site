from django.contrib import admin
from accounts.models import Publisher, Publication  


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'publisher', 'show']
    list_display_links = None
    list_editable = ['show']
    list_filter = ['publisher']

    pass
