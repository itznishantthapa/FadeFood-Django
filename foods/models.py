from django.db import models
from restaurant.models import restaurant

class food(models.Model):
    restaurant_name = models.ForeignKey(restaurant, on_delete=models.CASCADE,related_name='food')
    food_restaurant = models.CharField(max_length=100,blank=True, null=True)
    food_location = models.CharField(max_length=100,blank=True, null=True)
    food_name = models.CharField(max_length=100,blank=True, null=True)
    food_price = models.CharField(max_length=10,blank=True, null=True)
    rating = models.FloatField(default=0.0,blank=True, null=True)
    reviews = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    totol_eats = models.IntegerField(default=0)
    is_vegetarian=models.BooleanField(default=False)


class food_image(models.Model):
    food_itemforFK = models.ForeignKey(food, on_delete=models.CASCADE,related_name='foodimage')
    image = models.ImageField(upload_to='food_images/', blank=True, null=True)