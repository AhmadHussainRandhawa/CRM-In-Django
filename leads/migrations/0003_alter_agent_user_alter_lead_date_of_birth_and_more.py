# Generated by Django 5.1.7 on 2025-03-18 08:38

import django.db.models.deletion
import leads.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_agent_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='agent_profile', to=settings.AUTH_USER_MODEL, verbose_name='System User'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='date_of_birth',
            field=models.DateField(blank=True, help_text='YYYY-MM-DD', null=True, validators=[leads.models.validate_date_of_birth]),
        ),
        migrations.AlterField(
            model_name='lead',
            name='first_name',
            field=models.CharField(help_text="Enter the lead's first name", max_length=20, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='last_name',
            field=models.CharField(help_text="Enter the lead's last name", max_length=20, verbose_name='Last Name'),
        ),
        migrations.AddIndex(
            model_name='lead',
            index=models.Index(fields=['first_name', 'last_name'], name='leads_lead_first_n_a5a366_idx'),
        ),
    ]
