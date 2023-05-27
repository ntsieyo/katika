from django.contrib import admin

from tender.models import CDI_CRI, ArmpContract, ArmpEntry, Entreprise, EntrepriseChange, Exercice, TenderOwner, WBContract, WBProject, WBSupplier

# Register your models here.

class TenderOwnerAdmin(admin.ModelAdmin):

    list_display = ('owner_id', 'short_name', 'full_name')
    search_fields = ('owner_id', 'short_name', 'full_name')




class ArmpEntryAdmin(admin.ModelAdmin):

    list_display = ('owner', 'publication_datetime', 'cost', 'publication_type', 'title', 'link')
    search_fields = ('title', 'content')
    #search_fields = ('search_vector',)
    list_filter = ('owner', 'publication_datetime', 'publication_type')
    #filter_horizontal = ('supervisors', 'committee')
    #raw_id_fields = ('author',)


class CDI_CRIAdmin(admin.ModelAdmin):
    list_display = ("cdi", "cri", "matches")
    list_filter = ("cri",)
    search_fields = ("matches",)



class ExerciceAdmin(admin.ModelAdmin):

    list_display = ('year', 'month')
    search_fields = ('year', 'month')
    list_filter = ('year', 'month')




class EntrepriseAdmin(admin.ModelAdmin):

    list_display = ('niu', 'raison_sociale','sigle', 'regime', 'forme_juridique', 'ville', 'telephone')
    search_fields = ('raison_sociale', 'sigle', 'niu', 'telephone')
    list_filter = ('regime', 'forme_juridique', 'ville', 'departement', 'region', 'etat_niu')


class ArmpContractAdmin(admin.ModelAdmin):

    list_display = ('maitre_ouvrage', 'status','reference', 'title', 'date', 'year', 'cost', 'titulaire')
    search_fields = ('title', 'maitre_ouvrage', 'titulaire', 'reference')
    list_filter = ('status', 'maitre_ouvrage', 'year')


class WBProjectAdmin(admin.ModelAdmin):

    list_display = ('project_id', 'start_date', 'cost', 'name')
    search_fields = ('project_id', 'name', 'abstract', 'search_vector')
    list_filter = ('financial_type', 'status', 'agency')
    #exclude = ['search_vector']



class WBSupplierAdmin(admin.ModelAdmin):

    list_display = ('supplier_id', 'name')
    search_fields = ('supplier_id', 'name', 'search_vector')
    exclude = ['search_vector']




class WBContractAdmin(admin.ModelAdmin):

    list_display = ('date', 'get_project_id', 'cost', 'description')
    list_filter = ('project__project_id',)
    search_fields = ('search_vector',)





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