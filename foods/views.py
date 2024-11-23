from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import FoodSerializer
from authentications.permissions import IsSeller

@api_view(['POST'])
@permission_classes([IsSeller])
def add_food(request):
        try:
            restaurant= request.user.restaurant
            request.data['restaurant_name'] = restaurant.id
            serializer = FoodSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data,"msg":f"Food Added Successfully In {restaurant.name}"}, status=200)
            return Response(serializer.errors)
        except:
            return Response({"msg":"Something went wrong in the Backend"}, status=400)

@api_view(['PUT'])
@permission_classes([IsSeller])
def edit_food(request):
        try:
            restaurant= request.user.restaurant
            food = restaurant.food.get(id=request.data.get('id'))
            serializer = FoodSerializer(food, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data,"msg":"Food Info Update Successfully"}, status=200)
            return Response(serializer.errors)
        except:
            return Response({"msg":"Something went wrong in the Backend"}, status=400)
     
     
 
