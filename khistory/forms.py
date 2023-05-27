


from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, ButtonHolder, Submit

from khistory.models import Event, Personnage

class EventForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'History event',
                Div('date', 'importance'),
                'title',
                'content',
                Div('image_url', 'image_credits', 'image_caption'),
                'source'
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )
        super(EventForm, self).__init__(*args, **kwargs)

    date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )

    class Meta:
        model = Event
        exclude = Event.FORM_EXCLUDE


# class EventAdmin(admin.ModelAdmin):
#     class Meta:
#         form = EventForm

#admin.site.register(Event, EventAdmin)


class PersonnageForm(forms.ModelForm):

    birthday = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )

    # formfield_overrides = {
    #     'featured_image': {'widget': forms.ClearableFileInput},
    # }
    # featured_image = forms.ImageField(
    #     required=False,
    #     widget=forms.ClearableFileInput(
    #         attrs={
    #             'accept': ','.join(settings.ALLOWED_IMAGE_TYPES),
    #             'clear_checkbox_label': 'Remove custom cover'}
    #     ),
    # )
    # featured_image = forms.ImageField(required=False,
    #                                   error_messages={'invalid': _("Image files only")},
    #                  widget=forms.FileInput)

    class Meta:
        model = Personnage
        exclude = Personnage.FORM_EXCLUDE