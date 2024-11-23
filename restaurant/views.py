from django.shortcuts import render
from .serializers import RestaurantSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from authentications.permissions import IsSeller
from rest_framework.response import Response


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register_restaurant(request):
        try:
            owner = request.user
            request.data['owner'] = owner.id          
            serializer = RestaurantSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                owner.role = 'seller'
                owner.save(update_fields=['role'])
                return Response({"data":f"Restaurant Register Successfully In {owner.username} and he is {owner.role}"}, status=200)
            return Response(serializer.errors, status=400)
        except:
            return Response({"msg":"Something went wrong in the Backend"}, status=400)

@api_view(['PUT'])
@permission_classes([IsSeller])
def edit_restaurant(request):
        try:
            owner = request.user
            restaurant = owner.restaurant
            serializer = RestaurantSerializer(restaurant, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data,"msg":"Restaurant Info Update Successfully"}, status=200)
            return Response(serializer.errors, status=400)
        except:
            return Response({"msg":"Something went wrong in the Backend"}, status=400)

