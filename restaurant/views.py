from logging import exception
from django.shortcuts import render
from .serializers import RestaurantSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from authentications.permissions import IsSeller, IsCustomer
from rest_framework.response import Response
from .models import restaurant
from authentications.models import CustomUser


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register_restaurant(request):
        try:
            owner = request.user
            request.data['owner'] = owner.id  # (what if i use this kind of technqiue, huh GPT?)       
            serializer = RestaurantSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                owner.role = 'seller'
                owner.save(update_fields=['role'])
                return Response({"ofBackendData":f"Restaurant Register Successfully In {owner.username} and he is {owner.role}"}, status=200)
            return Response(serializer.errors, status=400)
        except:
            return Response({"msg":"Something went wrong in the Backend"}, status=400)

@api_view(['PUT'])
@permission_classes([IsSeller])
def edit_restaurant(request):
        try:
            user = request.user
            restaurant = user.restaurant
            serializer = RestaurantSerializer(restaurant, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"ofBackendData":serializer.data,"msg":"Restaurant Info Update Successfully"}, status=200)
            return Response(serializer.errors, status=400)
        except:
            return Response({"msg":"Something went wrong in the Backend"}, status=400)
        

@api_view(['GET'])
@permission_classes([IsSeller])
def get_restaurant(request):
        try:
            user = request.user
            restaurant = user.restaurant
            serializer = RestaurantSerializer(restaurant)
            return Response({'ofBackendData':serializer.data}, status=200)
        except:
            return Response({"msg":"Something went wrong in the Backend"}, status=400)
        
@api_view(['GET'])
def get_specific_restaurant(request):
        try:
            print('here1')
            restaurant_id = request.query_params.get('restaurant_name')
            print('here2',restaurant_id)
            restaurantObj = restaurant.objects.get(id=restaurant_id)
            print('here3')
            print('here3')
            serializer = RestaurantSerializer(restaurantObj)
            print('here4')
            return Response({'ofBackendData':serializer.data}, status=200)
        except:
            return Response({"msg":"Something went wrong in the Backend"}, status=400)