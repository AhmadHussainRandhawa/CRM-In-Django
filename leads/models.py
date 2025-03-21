from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.core.exceptions import ValidationError

class User(AbstractUser):
    pass


def validate_date_of_birth(value):
    # Ensure the dob is not in future
    if value > date.today():
        raise ValidationError("Date of birth can't be in the future")


class Lead(models.Model):
    first_name = models.CharField(max_length=150, verbose_name="First Name", help_text="Enter the lead's first name")
    last_name = models.CharField(max_length=150, verbose_name="Last Name",  help_text="Enter the lead's last name")
    date_of_birth = models.DateField(
        null=True, blank=True, help_text="YYYY-MM-DD", validators=[validate_date_of_birth])
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE, related_name="leads")

    class Meta:
        indexes = [models.Index(fields=['first_name', 'last_name'])]
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} (Agent: {self.agent.user.username if self.agent else 'unassigned'})"
    

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='agent_profile', verbose_name='System User')
    active = models.BooleanField(default=True, help_text="Is the agent still active?")

    def __str__(self):
        return f"{self.user.username}"

