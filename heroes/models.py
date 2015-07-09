from django.db import models

# Create your models here.
class Hero(models.Model):
    heroref = models.AutoField(primary_key=True)
    id = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50)
    localized_name = models.CharField(max_length=30)

