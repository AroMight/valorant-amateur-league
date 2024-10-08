# Generated by Django 5.1.1 on 2024-09-21 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0002_initial'),
        ('players', '0003_alter_player_tier'),
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='matches',
            field=models.ManyToManyField(related_name='players', through='stats.Stat', to='matches.match'),
        ),
    ]
