# Generated by Django 5.1.1 on 2024-09-26 10:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_initial_squashed_0005_alter_stat_match'),
        ('teams', '0003_alter_team_match'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stat',
            name='match',
        ),
        migrations.AlterField(
            model_name='stat',
            name='assists',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stat',
            name='deaths',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stat',
            name='kills',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stat',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stats', to='teams.team'),
        ),
        migrations.AlterUniqueTogether(
            name='stat',
            unique_together={('player', 'team')},
        ),
        migrations.AlterField(
            model_name='stat',
            name='ace',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='stat',
            name='mvp',
            field=models.BooleanField(default=False, null=True),
        ),
    ]