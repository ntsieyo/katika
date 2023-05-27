from django import forms

from incident.models import Incident
from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticOverlayMapWidget

class IncidentForm(forms.ModelForm):

    #TODO reposition Cameroon by default and zoom level
    #TODO at least 2 level down
    # location = geo_forms.PointField(widget=geo_forms.OSMWidget(attrs={'map_width':800,
    #                                                                   'map_height':500,
    #                                                                   ## default_zoom not working
    #                                                                   ## version too old?
    #                                                                   'default_zoom': 6,
    #                                                                   'default_lon': 13.3934,
    #                                                                   'default_lat': 9.3226,
    #                                                                   ## map_srid creates confusion
    #                                                                   ## potential bug
    #                                                                   ##'map_srid': 4326
    #                                                                   }))

    date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )

    class Meta:
        model = Incident
        fields = Incident.FORM_FIELDS

        widgets = {
            'location': GooglePointFieldWidget,
            'description': forms.Textarea(attrs={'rows': 8}),
            'notes': forms.Textarea(attrs={'rows': 3}),
            'tags': forms.SelectMultiple(attrs={'size': 8})
        }