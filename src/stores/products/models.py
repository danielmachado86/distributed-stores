from django.db import models

class Brand(models.Model):
    name = models.CharField()
    picture = models.CharField()

class Category(models.Model):
    name = models.CharField()
    parent = models.CharField()
    picture = models.CharField()

class Product(models.Model):
    name = models.CharField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
