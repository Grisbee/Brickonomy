# Generated by Django 4.2.7 on 2024-03-24 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_remove_minifigure_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='set',
            name='cover_image',
            field=models.ImageField(default='media/default_picture.jpg', upload_to='profile_pictures'),
        ),
    ]
