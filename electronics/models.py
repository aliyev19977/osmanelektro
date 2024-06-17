from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, blank='True', verbose_name="URL")

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    about = models.TextField(max_length=True, blank=True)
    photo = models.ImageField()
    price = models.IntegerField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, blank='True', verbose_name="URL")

    def __str__(self):
        return self.title
