from django.db import models
from django.contrib import admin
from django import forms


class Chapitre(models.Model):

    number = models.PositiveIntegerField(blank=True, null=True)
    short_name = models.CharField(max_length=20)
    full_name_fr = models.CharField(max_length=100, blank=True, null=True)
    full_name_en = models.CharField(max_length=100, blank=True, null=True)
    ADMIN_LIST_DISPLAY = ('number', 'short_name', 'full_name_fr', 'full_name_en')
    ADMIN_SEARCH_FIELDS = ('short_name', 'full_name_fr', 'full_name_en')
    ADMIN_LIST_FILTER = ('short_name',)

    def __str__(self):
        return self.short_name





class AnnualEntry(models.Model):

    year = models.PositiveIntegerField()
    chapitre = models.ForeignKey(Chapitre, blank=True, null=True, on_delete=models.SET_NULL)
    ae = models.BigIntegerField(blank=True, null=True)
    cp = models.BigIntegerField(blank=True, null=True)

    BF_BIP = [
        ('BF', 'Budget de Fonctionement'),
        ('BIP', "Budget d'Investissement")
    ]

    bf_bip = models.CharField(max_length=3, choices=BF_BIP)

    STATUS = [
        ('LF', 'Loi de Finance'),
        ('REV', 'Revised'),
        ('EX', 'Executed'),
    ]

    status = models.CharField(max_length=3, choices=STATUS)

    REGIONS = [
        ('EN', 'Extrême-Nord'),
        ('NO', 'Nord'),
        ('AD', 'Adamaoua'),
        ('LT', 'Littoral'),
        ('CE', 'Centre'),
        ('OU', 'Ouest'),
        ('NW', 'North-West'),
        ('SW', 'South-West'),
        ('SU', 'Sud'),
        ('ES', 'Est'),
        ('AC', 'Administration Centrale')
    ]

    region = models.CharField(max_length=3, choices=REGIONS)
    
    ADMIN_LIST_DISPLAY = ('chapitre', 'year', 'bf_bip', 'status', 'region', 'ae', 'cp')
    ADMIN_SEARCH_FIELDS = ('chapitre', 'region')
    ADMIN_LIST_FILTER = ('chapitre', 'year')

    class Meta:
        unique_together = ("year", "chapitre", "status", "region", 'bf_bip')



class BudgetProgramme(models.Model):
    year = models.PositiveIntegerField()
    chapitre = models.ForeignKey(Chapitre, blank=True, null=True, on_delete=models.SET_NULL)
    pg_id = models.CharField(max_length=20, blank=True, null=True)
    exercice_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.CharField(max_length=10)
    ae = models.BigIntegerField(blank=True, null=True)
    cp = models.BigIntegerField(blank=True, null=True)
    description_fr = models.TextField(blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)
    objective_fr = models.TextField(blank=True, null=True)
    objective_en = models.TextField(blank=True, null=True)
    indicator_fr = models.TextField(blank=True, null=True)
    indicator_en = models.TextField(blank=True, null=True)
    
    ADMIN_LIST_DISPLAY = ('chapitre', 'year', 'code', 'pg_id', 'ae', 'cp')
    ADMIN_SEARCH_FIELDS = ('chapitre', 'description_fr', 'objective_fr', 'indicator_fr')
    ADMIN_LIST_FILTER = ('chapitre', 'year', 'code')

    class Meta:

        unique_together = ("year", "chapitre", "code")



class BudgetProgrammeForm(forms.ModelForm):

    class Meta:
        model = BudgetProgramme
        fields = ('year', 'chapitre', 'ae', 'cp', 'code',
                  'description_fr', 'description_en',
                  'objective_fr', 'objective_en', 'indicator_fr', 'indicator_en')

        widgets = {
            'description_fr': forms.Textarea(attrs={'rows': 3}),
            'description_en': forms.Textarea(attrs={'rows': 3}),
            'objective_fr': forms.Textarea(attrs={'rows': 3}),
            'objective_en': forms.Textarea(attrs={'rows': 3}),
            'indicator_fr': forms.Textarea(attrs={'rows': 3}),
            'indicator_en': forms.Textarea(attrs={'rows': 3}),

        }