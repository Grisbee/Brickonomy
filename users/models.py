from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="media/default_picture.jpg", upload_to="profile_pictures")

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        min_dimension = min(img.width, img.height)
        img = img.crop((0, 0, min_dimension, min_dimension))

        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.image.path)

# Create your models here.
