# Generated by Django 3.2 on 2022-01-22 02:21

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_agent_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='user', unique=True),
        ),
    ]
