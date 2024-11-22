from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .permissions import IsSeller
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
@api_view(['POST'])
def create_user(request):
        data=request.data
        username = data.get('email')
        password = data.get('password')
        email = data.get('email')
        role = data.get('role', 'customer')
        name = data.get('name')
        phone = data.get('phone')

        if CustomUser.objects.filter(username=username).exists():
                 return Response({'msg': 'Email already exists'}, status=400)
        
        user = CustomUser.objects.create_user(username=username, password=password, email=email,role=role,name=name,phone=phone)
        user.save()
        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token
        return Response({"msg":"Account Created Successfully","access":str(access_token),"refresh":str(refresh)},status=200)



@api_view(['GET'])
# @permission_classes([IsSeller])
@permission_classes([IsAuthenticated])
def get_user_details(request):
        user=request.user
        return Response({"data":{'username':user.name,'role':user.role},'msg':'We Send You --> Name and Role'},status=200)