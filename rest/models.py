from django.db import models
from django.utils import timezone


class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    event = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.restaurant_name

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=150)
    # created_at = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.menu_name

class Food(models.Model):
    id = models.AutoField(primary_key=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=20)
    rating = models.FloatField()
    
    def __str__(self):
        return self.food_name