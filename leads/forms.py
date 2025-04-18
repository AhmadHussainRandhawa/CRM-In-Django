from django import forms
from .models import Lead
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()

class LeadModelForm(forms.ModelForm):
    class Meta:
        model=Lead
        fields = ['first_name', 'last_name', 'date_of_birth', 'organization', 'agent']
        widgets={ 'date_of_birth': forms.DateInput(attrs={'type':'date'})}
        

class CustomeUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}

