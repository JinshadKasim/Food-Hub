from django.db import models

# Create your models here.

class Orders(models.Model):
    name = models.CharField(max_length=100)
    number = models.BigIntegerField()
    address = models.CharField(max_length=100)
    food_details = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    class Meta:
        db_table = 'orders'
