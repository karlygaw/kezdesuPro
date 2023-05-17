from django.contrib import admin

from .models import *

class MeetingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'date', 'time_create')

admin.site.register(MeetingSphere, MeetingAdmin)
admin.site.register(Category)
admin.site.register(Cuisine)
admin.site.register(Place)
