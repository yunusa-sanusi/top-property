# Generated by Django 3.2 on 2022-01-24 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0006_auto_20220124_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='price',
            field=models.CharField(default=15000, max_length=20),
            preserve_default=False,
        ),
    ]