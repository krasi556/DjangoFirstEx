from django.contrib import admin

from people.models import People


# Register your models here.

@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    pass