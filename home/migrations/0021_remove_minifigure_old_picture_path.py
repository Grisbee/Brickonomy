# Generated by Django 4.2.7 on 2024-03-25 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_minifigure_old_picture_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='minifigure',
            name='old_picture_path',
        ),
    ]
