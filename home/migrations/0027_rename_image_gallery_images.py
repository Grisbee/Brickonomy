# Generated by Django 4.2.7 on 2024-03-26 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_gallery_remove_minifigure_gallery_image_delete_file_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='image',
            new_name='images',
        ),
    ]
