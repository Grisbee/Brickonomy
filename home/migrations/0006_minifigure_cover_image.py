# Generated by Django 4.2.7 on 2024-03-24 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_set_owner_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='minifigure',
            name='cover_image',
            field=models.ImageField(default='minifigure_default.png', upload_to='minifigure_cover'),
        ),
    ]
