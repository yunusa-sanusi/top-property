# Generated by Django 3.2 on 2022-01-22 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='social_account',
            name='url',
        ),
        migrations.AddField(
            model_name='social_account',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='social_account',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='social_account',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='social_account',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
    ]