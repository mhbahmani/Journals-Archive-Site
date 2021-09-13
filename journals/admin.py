from django.contrib import admin

from journals.models import Publication


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'publisher', 'show']
    list_display_links = None
    list_editable = ['show']
    list_filter = ['publisher']