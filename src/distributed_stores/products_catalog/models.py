from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=120)
    picture = models.CharField(max_length=256)
    description = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length=120)
    parent = models.CharField(max_length=120)
    picture = models.CharField(max_length=120)
    description = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=120)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
