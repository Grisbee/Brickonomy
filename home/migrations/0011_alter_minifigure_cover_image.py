# Generated by Django 4.2.7 on 2024-03-24 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_minifigure_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minifigure',
            name='cover_image',
            field=models.ImageField(default='default_picture.jpg', upload_to='profile_pictures'),
        ),
    ]
