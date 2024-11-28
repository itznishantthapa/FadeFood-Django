# from django.contrib import admin
# from .models import food, food_image

# admin.site.register(food )
# admin.site.register(food_image )

from django.contrib import admin
from .models import food ,food_image

class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'food_name', 'restaurant_name', 'food_price', 'is_available', 'rating', 'totol_eats')



admin.site.register(food, FoodAdmin)
admin.site.register(food_image)
