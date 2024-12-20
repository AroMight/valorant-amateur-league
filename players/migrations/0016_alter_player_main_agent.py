# Generated by Django 5.1.1 on 2024-11-29 22:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamedata', '0016_map_splash'),
        ('players', '0015_alter_player_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='main_agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gamedata.agent'),
        ),
    ]
