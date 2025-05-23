from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save


class User(AbstractUser):
    is_organizer = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

def validate_date_of_birth(value):
    # Ensure the dob is not in future
    if value > date.today():
        raise ValidationError("Date of birth can't be in the future")

class Lead(models.Model):
    first_name = models.CharField(max_length=150, verbose_name="First Name")
    last_name = models.CharField(max_length=150, verbose_name="Last Name")
    date_of_birth = models.DateField(
        null=True, blank=True, validators=[validate_date_of_birth])
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.SET_NULL)
    # description = models.TextField()
    # date_added = models.DateTimeField(auto_now_add=True)
    # phone_number = models.CharField(max_length=20)
    # email = models.EmailField()

    class Meta:
        indexes = [models.Index(fields=['first_name', 'last_name'])]
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} (Agent: {self.agent.user.username if self.agent else 'unassigned'})"
    

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    active = models.BooleanField(default=True, )
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)


class Category(models.Model):
    name = models.CharField(max_length=150)     # New, Contacted, converted, unconverted
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name