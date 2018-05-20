from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from datetime import date

class User(AbstractUser):

    name = models.CharField(max_length = 30)
    

class Restaurant(models.Model):
    user = models.ForeignKey(User, default=1,on_delete=models.CASCADE,)
    date = models.DateField(default=date.today)
    name = models.TextField()
    review = models.IntegerField(blank=True, null=True)
    street = models.TextField(blank=True, null=True)
    city = models.TextField(default="")
    zipCode = models.TextField(blank=True, null=True)
    State = models.TextField(blank=True, null=True)

class Dish(models.Model):
    name = models.TextField()
    review = models.IntegerField(blank=True, null=True)
    price = models.DecimalField('Dollar amount', max_digits=8, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(User, default=1,on_delete=models.CASCADE,)
    date = models.DateField(default=date.today)
    restaurant = models.ForeignKey(Restaurant, null=True, related_name='dishes',on_delete=models.CASCADE,)


class Meta:
        abstract = True

class Room(models.Model):
 

    title = models.CharField(max_length=255)

    staff_only = models.BooleanField(default=False)

    def str(self):
        return self.title