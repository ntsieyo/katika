from django.contrib import admin

from covid19.models import CovidCategory, CovidFund, CovidInitiative, CovidProducer

# Register your models here.

class CovidProductAdmin(admin.ModelAdmin):

    list_display = CovidProducer.ADMIN_LIST_DISPLAY
    search_fields = CovidProducer.ADMIN_SEARCH_FIELDS
    list_filter = CovidProducer.ADMIN_LIST_FILTER
    #filter_horizontal = ('supervisors', 'committee')
    #raw_id_fields = ('author',)


class CovidCatalogAdmin(admin.ModelAdmin):

    fields = CovidCategory.ADMIN_FIELDS

    list_display = CovidCategory.ADMIN_LIST_DISPLAY


class CovidInitiativeAdmin(admin.ModelAdmin):

    #fields = ['name',]

    list_display = CovidInitiative.ADMIN_LIST_DISPLAY
    

class CovidFundAdmin(admin.ModelAdmin):

    list_display = CovidFund.ADMIN_LIST_DISPLAY




admin.site.register(CovidProducer, CovidProductAdmin)
admin.site.register(CovidCategory, CovidCatalogAdmin)
admin.site.register(CovidInitiative, CovidInitiativeAdmin)
admin.site.register(CovidFund, CovidFundAdmin)