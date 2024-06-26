from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from PIL import Image
import os
from django import forms


class Set(models.Model):
    name = models.CharField(max_length=20, editable=True)
    if_moc = models.BooleanField(editable=True)
    era = models.CharField(max_length=15)
    description = models.TextField()
    estimated_price = models.FloatField()
    quantity = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=20, default='default_user')

    def save(self, *args, **kwargs):
        if self.owner:
            self.owner_name = self.owner.username
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name


class Minifigure(models.Model):
    ERA_CHOICES = (("option1", "Prequels"), ("option2", "Original Trilogy"), ("option3", "Sequels"),
                   ("option4", "Clone Wars"), ("option5", "Rebels"), ("option6", "TV Series"),
                   ("option7", "Legends"), ("option8", "Games"), ("option9", "Other"))

    character_name = models.CharField(max_length=30)
    if_custom = models.BooleanField()
    era = models.CharField(max_length=20, choices=ERA_CHOICES)
    description = models.TextField()
    estimated_price = models.FloatField()
    quantity = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default="minifigure_default.png", upload_to="minifigure_cover")

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=20, default='default_user')

    def __str__(self):
        return self.character_name

    def save(self, *args, **kwargs):
        if self.owner:
            self.owner_name = self.owner.username
        try:
            old_instance = Minifigure.objects.get(pk=self.pk)
            if old_instance.image != self.image:

                if os.path.isfile(old_instance.image.path):
                    os.remove(old_instance.image.path)
        except Minifigure.DoesNotExist:
            pass

        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        min_dimension = min(img.width, img.height)
        img = img.crop((0, 0, min_dimension, min_dimension))

        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.image.path)


    def get_absolute_url(self):
        return reverse("minifigures-post", kwargs={'pk': self.pk})


class Gallery(models.Model):
    minifigure = models.ForeignKey(Minifigure, on_delete=models.CASCADE)
    images = models.ImageField(default="minifigure_default.png", upload_to="gallery")

#to niżej dodane
    def save(self, *args, **kwargs):
        if self.minifigure.gallery_set.count() < 5:
            super().save(*args, **kwargs)

            img = Image.open(self.images.path)
            min_dimension = min(img.width, img.height)
            img = img.crop((0, 0, min_dimension, min_dimension))

            if img.height > 512 or img.width > 512:
                output_size = (512, 512)
                img.thumbnail(output_size)
                img.save(self.images.path)

            #dodać else żeby wyrzucało jakiś error czy coś


