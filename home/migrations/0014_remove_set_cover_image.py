# Generated by Django 4.2.7 on 2024-03-24 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_set_cover_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='set',
            name='cover_image',
        ),
    ]
