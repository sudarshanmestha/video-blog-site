# Generated by Django 4.2.11 on 2024-03-16 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0003_post_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
