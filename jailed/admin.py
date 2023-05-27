from django.contrib import admin
from django.contrib.gis.db import models as geo_models
from mapwidgets.widgets import GooglePointFieldWidget

from jailed.models import Incarceration, IncarcerationTag, Judge, Prison

# Register your models here.


class IncarcerationAdmin(admin.ModelAdmin):

    list_display = Incarceration.ADMIN_LIST_DISPLAY
    search_fields = Incarceration.ADMIN_SEARCH_FIELDS


class PrisonAdmin(admin.ModelAdmin):

    fiels = Prison.ADMIN_FIELDS

    formfield_overrides = {
        geo_models.PointField: {"widget": GooglePointFieldWidget},
        # KeywordsField: {"widget": KeywordsWidget},

    }


admin.site.register(IncarcerationTag)
admin.site.register(Prison, PrisonAdmin)

admin.site.register(Incarceration, IncarcerationAdmin)
admin.site.register(Judge)