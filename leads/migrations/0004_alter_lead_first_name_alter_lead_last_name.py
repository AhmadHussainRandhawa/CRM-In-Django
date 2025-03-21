# Generated by Django 5.1.7 on 2025-03-21 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_alter_agent_user_alter_lead_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='first_name',
            field=models.CharField(help_text="Enter the lead's first name", max_length=150, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='last_name',
            field=models.CharField(help_text="Enter the lead's last name", max_length=150, verbose_name='Last Name'),
        ),
    ]
