# Generated by Django 5.1.1 on 2024-10-18 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0010_alter_stat_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='stat',
            name='first_bloods',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stat',
            name='plants',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stat',
            name='spikes_defused',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
