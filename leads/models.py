from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date


class User(AbstractUser):
    pass


class Lead(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="First Name")
    last_name = models.CharField(max_length=20, verbose_name="Last Name")
    date_of_birth = models.DateField(null=True, blank=True)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE, related_name="leads")

    @property
    def age(self):
        if not self.date_of_birth: 
            return None 

        today = date.today()
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

    def __str__(self):
        return f"{self.first_name} has assigned to Agent {self.agent.user.username}"
    

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='agent_profile')

    def __str__(self):
        return self.user.username
