from django import forms

class LeadForm(forms.Form):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    
