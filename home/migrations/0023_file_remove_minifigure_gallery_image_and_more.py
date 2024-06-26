# Generated by Django 4.2.7 on 2024-03-26 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_minifigure_gallery_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='gallery')),
            ],
        ),
        migrations.RemoveField(
            model_name='minifigure',
            name='gallery_image',
        ),
        migrations.AddField(
            model_name='minifigure',
            name='gallery_image',
            field=models.ManyToManyField(to='home.file'),
        ),
    ]
