# Generated by Django 3.2 on 2022-01-22 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_agent_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='social_account',
            name='agent',
        ),
        migrations.DeleteModel(
            name='Agent',
        ),
        migrations.DeleteModel(
            name='Social_Account',
        ),
    ]
