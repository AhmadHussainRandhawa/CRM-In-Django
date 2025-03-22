from django import forms
from .models import Lead

class LeadModelForm(forms.ModelForm):
    class Meta:
        model=Lead
        fields = ['first_name', 'last_name', 'date_of_birth', 'agent']
        widgets={ 'date_of_birth': forms.DateInput(attrs={'type':'date'})}
        help_texts = {'date_of_birth': ''}
