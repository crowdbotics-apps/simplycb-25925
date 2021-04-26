from django.contrib import admin

from apps.models import App


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    pass
