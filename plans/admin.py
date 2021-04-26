from django.contrib import admin

from plans.models import Plan


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    pass
