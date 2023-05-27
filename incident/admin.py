from django.contrib import admin
from django.contrib.gis.db import models as geo_models
from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticOverlayMapWidget

from incident.models import Incident, IncidentType, KeySource, Tag

# Register your models here.


class IncidentTypeAdmin(admin.ModelAdmin):

    # fields = ['name', 'age', 'residence']
    fields = IncidentType.ADMIN_FIELDS


class IncidentAdmin(admin.ModelAdmin):

    # fields = ['name', 'age', 'residence']
    #fieldset = {'address', fields = ['type', 'location', 'date', 'description', 'source', 'deaths', 'wounded']
    exclude = Incident.ADMIN_EXCLUDE
    formfield_overrides = {
        geo_models.PointField: {"widget": GooglePointFieldWidget},
        #KeywordsField: {"widget": KeywordsWidget},

    }

    list_display = Incident.ADMIN_LIST_DISPLAY
    search_fields = Incident.ADMIN_SEARCH_FIELDS
    list_filter = Incident.ADMIN_LIST_FILTER



admin.site.register(IncidentType, IncidentTypeAdmin)
admin.site.register(Tag)
admin.site.register(KeySource)
admin.site.register(Incident, IncidentAdmin)