from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
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
    character_name = models.CharField(max_length=30)
    if_custom = models.BooleanField()
    era = models.CharField(max_length=15)
    description = models.TextField()
    estimated_price = models.FloatField()
    quantity = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=20, default='default_user')

    def __str__(self):
        return self.character_name

    def save(self, *args, **kwargs):
        if self.owner:
            self.owner_name = self.owner.username
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("minifigures-post", kwargs={'pk': self.pk})
