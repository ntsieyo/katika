from django import forms

from budget.models import BudgetProgramme


class BudgetProgrammeForm(forms.ModelForm):

    class Meta:
        model = BudgetProgramme
        fields = BudgetProgramme.FORM_FIELDS

        widgets = {
            'description_fr': forms.Textarea(attrs={'rows': 3}),
            'description_en': forms.Textarea(attrs={'rows': 3}),
            'objective_fr': forms.Textarea(attrs={'rows': 3}),
            'objective_en': forms.Textarea(attrs={'rows': 3}),
            'indicator_fr': forms.Textarea(attrs={'rows': 3}),
            'indicator_en': forms.Textarea(attrs={'rows': 3}),

        }