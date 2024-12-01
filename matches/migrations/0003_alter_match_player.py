# Generated by Django 5.1.3 on 2024-12-01 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0002_alter_match_options'),
        ('players', '0002_atpplayers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='players.atpplayers'),
        ),
    ]