# Generated by Django 4.2.7 on 2024-03-17 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_minifigure_owner_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='set',
            name='owner_name',
            field=models.CharField(default='default_user', max_length=20),
        ),
    ]