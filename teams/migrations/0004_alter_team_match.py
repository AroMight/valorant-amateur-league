# Generated by Django 5.1.1 on 2024-10-27 17:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0013_remove_match_url_match_youtube_url'),
        ('teams', '0003_alter_team_match'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='match',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='matches.match'),
        ),
    ]
