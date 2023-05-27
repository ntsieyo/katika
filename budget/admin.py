from django.contrib import admin

from budget.models import AnnualEntry, BudgetProgramme, Chapitre

# Register your models here.

class ChapitreAdmin(admin.ModelAdmin):

    list_display = Chapitre.ADMIN_LIST_DISPLAY
    search_fields = Chapitre.ADMIN_SEARCH_FIELDS
    list_filter = Chapitre.ADMIN_LIST_FILTER


class AnnualEntryAdmin(admin.ModelAdmin):

    list_display = AnnualEntry.ADMIN_LIST_DISPLAY
    search_fields = AnnualEntry.ADMIN_SEARCH_FIELDS
    list_filter = AnnualEntry.ADMIN_LIST_FILTER


class BudgetProgrammeAdmin(admin.ModelAdmin):

    list_display = BudgetProgramme.ADMIN_LIST_DISPLAY
    search_fields = BudgetProgramme.ADMIN_SEARCH_FIELDS
    list_filter = BudgetProgramme.ADMIN_LIST_FILTER



admin.site.register(BudgetProgramme, BudgetProgrammeAdmin)
admin.site.register(Chapitre, ChapitreAdmin)
admin.site.register(AnnualEntry, AnnualEntryAdmin)