from django.db import models

# Create your models here.
class Item(models.Model):
    itemref = models.AutoField(primary_key=True)
    id = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=60)
    cost = models.PositiveIntegerField()
    secret_shop = models.PositiveSmallIntegerField()
    side_shop = models.PositiveSmallIntegerField()
    recipe = models.PositiveSmallIntegerField()
    localized_name = models.CharField(max_length=60)
