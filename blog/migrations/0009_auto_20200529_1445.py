# Generated by Django 3.0.6 on 2020-05-29 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200529_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body_de',
        ),
        migrations.RemoveField(
            model_name='post',
            name='body_en',
        ),
        migrations.RemoveField(
            model_name='post',
            name='body_fr',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_de',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_fr',
        ),
    ]
