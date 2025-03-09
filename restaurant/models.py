from django.db import models
from authentications.models import CustomUser

class restaurant(models.Model):
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE,related_name='restaurant')
    name = models.CharField(max_length=100,blank=True,null=True)
    phone=models.CharField(max_length=100,blank=True,null=True)
    street_address=models.CharField(max_length=100,blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    citizenship_number=models.CharField(max_length=100,blank=True,null=True)
    pan_number=models.CharField(max_length=100,blank=True,null=True)
    business_type=models.CharField(max_length=100,blank=True,null=True)
    opening_hour=models.CharField(max_length=10,blank=True,null=True)
    logo = models.ImageField(upload_to='restaurants/logos/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='restaurants/cover_images/', blank=True, null=True)
    is_active = models.BooleanField(default=False)  # New field to distinguish restaurants
    restaurant_images = models.ImageField(upload_to='restaurants/images/', blank=True)
    rating = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)

    def __str__(self): 
        return self.name

