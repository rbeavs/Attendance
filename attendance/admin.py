from django.contrib import admin
from .models import Snippet, Event
from django.urls import path
from .views import archive


class ArchiveAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'FR', 'SO', 'JR', 'SR', 'points', 'event', 'created_at')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('archive/<int:year>/<int:month>/<int:day>/', self.admin_site.admin_view(archive), name='archive'),
        ]
        return my_urls + urls


class EventAdmin(admin.ModelAdmin):
    list_display = ['events', ]

admin.site.register(Snippet, ArchiveAdmin)
admin.site.register(Event, EventAdmin)
