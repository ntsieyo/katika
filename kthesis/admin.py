from django.contrib import admin

from kthesis.models import Degree, KeywordEn, KeywordFr, Scholar, Thesis, University

# Register your models here.


class ScholarAdmin(admin.ModelAdmin):
    list_display = Scholar.ADMIN_LIST_DISPLAY
    search_fields = Scholar.ADMIN_SEARCH_FIELDS



class ThesisAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'year', 'university')
    search_fields = ('title', 'author')
    list_filter = ('university', 'year')
    filter_horizontal = ('supervisors', 'committee')
    raw_id_fields = ('author',)



admin.site.register(Scholar, ScholarAdmin)
admin.site.register(Degree)
admin.site.register(University)
admin.site.register(KeywordEn)
admin.site.register(KeywordFr)
admin.site.register(Thesis, ThesisAdmin)