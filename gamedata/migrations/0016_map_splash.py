# Generated by Django 5.1.1 on 2024-10-26 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamedata', '0015_remove_map_splash_alter_agent_background_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='splash',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]