# Generated by Django 4.2.11 on 2024-03-19 07:19

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0005_post_body'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='post',
            name='order',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
    ]
