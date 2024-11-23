from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import FoodSerializer
from .models import food
from authentications.permissions import IsSeller ,IsCustomer

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
        
@api_view(['GET'])
@permission_classes([IsSeller])
def get_food(request):
        try:
            restaurant = request.user.restaurant  # Access Restaurant via reverse OneToOneField
            foods = restaurant.food.all()
            serializer = FoodSerializer(foods, many=True)
            return Response({"data":serializer.data}, status=200)
        except Exception as e:
            return Response({"msg":str(e)}, status=400)

@api_view(['PUT'])
@permission_classes([IsSeller])
def edit_food(request):
        try:
            restaurant = request.user.restaurant  # Access Restaurant via reverse OneToOneField
            food_id = request.data.get('id')

            # Fetch Food item belonging to the restaurant
            food = restaurant.food.filter(id=food_id).first()

            serializer = FoodSerializer(food, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data,"msg":"Food Info Update Successfully"}, status=200)
            return Response(serializer.errors)
        except Exception as e:
            return Response({"msg":str(e)}, status=400)

@api_view(['DELETE'])
@permission_classes([IsSeller])
def delete_food(request):
        try:
            restaurant = request.user.restaurant  # Access Restaurant via reverse OneToOneField
            food_id = request.data.get('id')

            # Fetch Food item belonging to the restaurant
            food = restaurant.food.filter(id=food_id).first()
            food.delete()
            return Response({"msg":"Food Deleted Successfully"}, status=200)
        except Exception as e:
            return Response({"msg":str(e)}, status=400)
        

@api_view(['GET'])
@permission_classes([IsCustomer])
def get_all_food(request):
        try:
            foods = food.objects.all()
            serializer = FoodSerializer(foods, many=True)
            return Response({"data":serializer.data}, status=200)
        except Exception as e:
            return Response({"msg":str(e)}, status=400)
