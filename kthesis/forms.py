from django import forms

from kthesis.models import Scholar, Thesis

class ScholarForm(forms.ModelForm):

    class Meta:
        model = Scholar
        exclude = Scholar.FORM_EXCLUDE_FIELDS


class ThesisForm(forms.ModelForm):

    class Meta:
        model = Thesis
        exclude = Thesis.FORM_EXCLUDE_FIELDS
        labels = {
            'title' : 'Title (in English)',
            'title_fr': 'Titre (en Français)',
            'year': 'Year (Année de soutenance)',
            'abstract_fr': 'Résumé',
            'keywords_fr': 'Mots clés',
        }
        widgets = {
            'title': forms.Textarea(attrs={'rows':1}),
            'title_fr': forms.Textarea(attrs={'rows': 1}),
        }