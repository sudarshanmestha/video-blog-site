# Generated by Django 4.2.11 on 2024-03-19 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='timeline',
            field=models.IntegerField(default=12, max_length=20),
            preserve_default=False,
        ),
    ]
