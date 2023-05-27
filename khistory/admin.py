from django.contrib import admin

from khistory.models import Event, Personnage

# Register your models here.


admin.site.register(Personnage)
admin.site.register(Event)