from django.contrib import admin
from calcs.models import Ohms 



@admin.register(Ohms)
class OhmsAdmin(admin.ModelAdmin):
    list_display = ('voltage', 'current', 'resistance')