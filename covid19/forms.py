from django import forms

from covid19.models import CovidFund, CovidInitiative, CovidProducer


class CovidProducerForm(forms.ModelForm):

    class Meta:
        model = CovidProducer
        fields = CovidProducer.FORM_FIELDS


class CovidInitiativeForm(forms.ModelForm):

    class Meta:
        model = CovidInitiative
        fields = CovidInitiative.FORM_FIELDS



class CovidFundForm(forms.ModelForm):

    class Meta:
        model = CovidFund
        fields = CovidFund.FORM_FIELDS
