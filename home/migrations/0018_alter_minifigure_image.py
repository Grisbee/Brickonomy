# Generated by Django 4.2.7 on 2024-03-24 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_minifigure_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minifigure',
            name='image',
            field=models.ImageField(default='minifigure_default.png', upload_to='minifigure_cover'),
        ),
    ]
