from django import forms
from .models import Lead, Agent
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


class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=User.objects.none(), label="Assign Agent")

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        agent = Agent.objects.filter(organization=request.user.userprofile)
        
        super().__init__(*args, **kwargs)
        self.fields['agent'].queryset = agent
 

class LeadCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['category']