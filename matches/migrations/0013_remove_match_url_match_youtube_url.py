# Generated by Django 5.1.1 on 2024-10-21 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0012_alter_match_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='url',
        ),
        migrations.AddField(
            model_name='match',
            name='youtube_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
