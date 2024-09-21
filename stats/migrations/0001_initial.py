# Generated by Django 5.1.1 on 2024-09-21 14:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gamedata', '0005_alter_role_icon'),
        ('matches', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kills', models.IntegerField(null=True)),
                ('deaths', models.IntegerField(null=True)),
                ('assists', models.IntegerField(null=True)),
                ('mvp', models.BooleanField(null=True)),
                ('ace', models.BooleanField(null=True)),
                ('agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stats', to='gamedata.agent')),
                ('match', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stats', to='matches.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stats', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
