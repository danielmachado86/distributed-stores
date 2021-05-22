from django.db import models

from treebeard.al_tree import AL_Node

class Brand(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True, null=True)
    picture = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Category(AL_Node):
    name = models.CharField(max_length=30)
    parent = models.ForeignKey('self',
                               related_name='children_set',
                               null=True,
                               blank=True,
                               db_index=True,
                               on_delete=models.CASCADE)

    node_order_by = ['name']

    def __str__(self):
        return 'Category: {}'.format(self.name)

# class Category(models.Model):
#     name = models.CharField(max_length=120)
#     parent = models.CharField(max_length=120, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     picture = models.URLField(blank=True, null=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         unique_together = ('name', 'parent')


class Product(models.Model):
    name = models.CharField(max_length=120)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    picture = models.URLField(blank=True ,null=True)

    def __str__(self):
        return self.brand.name + ' ' + self.name

    class Meta:
        unique_together = ('name', 'brand')


class ProductSpecs(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.CharField(max_length=30)
    value = models.CharField(max_length=140)


    def __str__(self):
        return self.product.name + ' ' + self.attribute

    class Meta:
        unique_together = ('product', 'attribute')