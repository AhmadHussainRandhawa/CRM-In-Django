# Generated by Django 5.1.7 on 2025-04-25 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0004_alter_agent_user_alter_lead_agent_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='lead',
            old_name='Category',
            new_name='category',
        ),
    ]
