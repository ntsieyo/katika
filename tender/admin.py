from django.contrib import admin

from tender.models import CDI_CRI, ArmpContract, ArmpEntry, Entreprise, EntrepriseChange, Exercice, TenderOwner, WBContract, WBProject, WBSupplier

# Register your models here.

class TenderOwnerAdmin(admin.ModelAdmin):

    list_display = TenderOwner.ADMIN_LIST_DISPLAY
    search_fields = TenderOwner.ADMIN_SEARCH_FIELDS




class ArmpEntryAdmin(admin.ModelAdmin):

    list_display = ArmpEntry.ADMIN_LIST_DISPLAY
    search_fields = ArmpEntry.ADMIN_SEARCH_FIELDS
    list_filter = ArmpEntry.ADMIN_LIST_FILTER


class CDI_CRIAdmin(admin.ModelAdmin):
    list_display = CDI_CRI.ADMIN_LIST_DISPLAY
    search_fields = CDI_CRI.ADMIN_SEARCH_FIELDS
    list_filter = CDI_CRI.ADMIN_LIST_FILTER



class ExerciceAdmin(admin.ModelAdmin):

    list_display = Exercice.ADMIN_LIST_DISPLAY
    search_fields = Exercice.ADMIN_SEARCH_FIELDS
    list_filter = Exercice.ADMIN_LIST_FILTER




class EntrepriseAdmin(admin.ModelAdmin):

    list_display = Entreprise.ADMIN_LIST_DISPLAY
    search_fields = Entreprise.ADMIN_SEARCH_FIELDS
    list_filter = Entreprise.ADMIN_LIST_FILTER


class ArmpContractAdmin(admin.ModelAdmin):

    list_display = ArmpContract.ADMIN_LIST_DISPLAY
    search_fields = ArmpContract.ADMIN_SEARCH_FIELDS
    list_filter = ArmpContract.ADMIN_LIST_FILTER


class WBProjectAdmin(admin.ModelAdmin):

    list_display = WBProject.ADMIN_LIST_DISPLAY
    search_fields = WBProject.ADMIN_SEARCH_FIELDS
    list_filter = WBProject.ADMIN_LIST_FILTER



class WBSupplierAdmin(admin.ModelAdmin):

    list_display = WBSupplier.ADMIN_LIST_DISPLAY
    search_fields = WBSupplier.ADMIN_SEARCH_FIELDS
    exclude = WBSupplier.ADMIN_LIST_EXCLUDE




class WBContractAdmin(admin.ModelAdmin):

    list_display = WBContract.ADMIN_LIST_DISPLAY
    search_fields = WBContract.ADMIN_SEARCH_FIELDS
    list_filter = WBContract.ADMIN_LIST_FILTER





admin.site.register(TenderOwner, TenderOwnerAdmin)

admin.site.register(WBContract, WBContractAdmin)
admin.site.register(WBSupplier, WBSupplierAdmin)

admin.site.register(WBProject, WBProjectAdmin)

admin.site.register(ArmpContract, ArmpContractAdmin)
admin.site.register(ArmpEntry, ArmpEntryAdmin)

admin.site.register(Entreprise, EntrepriseAdmin)
admin.site.register(EntrepriseChange)

admin.site.register(Exercice, ExerciceAdmin)
admin.site.register(CDI_CRI, CDI_CRIAdmin)