# Generated by Django 5.1.1 on 2024-09-22 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamedata', '0002_alter_agent_background_alter_agent_full_portrait_and_more_squashed_0009_rename_list_horintal_icon_map_list_horizontal_icon'),
        ('players', '0006_remove_player_matches'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='tier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='players', to='gamedata.tier'),
        ),
    ]