# from rest_framework import serializers
# from .models import food , food_image

# class FoodSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = food
#         fields = '__all__'

# class FoodImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = food_image
#         fields = '__all__'

from rest_framework import serializers
from .models import food, food_image

class FoodImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = food_image
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    images = FoodImageSerializer(source='foodimage', many=True)  # Use related_name 'foodimage'

    class Meta:
        model = food
        fields = '__all__'

