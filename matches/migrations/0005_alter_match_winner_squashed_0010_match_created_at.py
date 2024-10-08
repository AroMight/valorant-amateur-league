# Generated by Django 5.1.1 on 2024-09-26 13:38

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("matches", "0004_alter_match_map_alter_match_winner"),
        ("teams", "0003_alter_team_match"),
    ]

    operations = [
        migrations.AlterField(
            model_name="match",
            name="winner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="matches",
                to="teams.team",
            ),
        ),
        migrations.AddField(
            model_name="match",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
