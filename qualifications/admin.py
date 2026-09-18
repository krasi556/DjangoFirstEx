from django.contrib import admin

from qualifications.models import Qualifications


# Register your models here.

@admin.register(Qualifications)
class QualificationsAdmin(admin.ModelAdmin):
    list_display = ['courses','university']