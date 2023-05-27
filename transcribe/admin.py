from django.contrib import admin

from transcribe.models import Transcript

# Register your models here.

#class TranscriptAdmin(admin.ModelAdmin):
#    pass


#admin.site.register(Transcript, TranscriptAdmin)
admin.site.register(Transcript)