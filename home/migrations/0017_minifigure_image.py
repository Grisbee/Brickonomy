# Generated by Django 4.2.7 on 2024-03-24 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_remove_minifigure_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='minifigure',
            name='image',
            field=models.ImageField(default='default_picture.jpg', upload_to='profile_pictures'),
        ),
    ]
