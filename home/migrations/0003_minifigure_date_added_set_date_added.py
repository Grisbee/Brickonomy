# Generated by Django 4.2.7 on 2024-03-15 15:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_if_custom_set_if_moc'),
    ]

    operations = [
        migrations.AddField(
            model_name='minifigure',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='set',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
