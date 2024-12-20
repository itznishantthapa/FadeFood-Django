from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from .models import CustomUser
from .permissions import IsSeller
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
@api_view(['POST'])
def create_user(request):
        try:
                data=request.data
                username = data.get('email')
                password = data.get('password')
                email = data.get('email')
                role = data.get('role', 'customer')
                name = data.get('name')
                phone = data.get('phone')
                profile_pic = data.get('profile_pic')

                if CustomUser.objects.filter(username=username).exists():
                        return Response({'msg': 'Email already exists'}, status=400)
                
                user = CustomUser.objects.create_user(username=username, password=password, email=email,role=role,name=name,phone=phone,profile_pic=profile_pic)
                user.save()
                refresh = RefreshToken.for_user(user)
                access_token = refresh.access_token
                return Response({"msg":"Account Created Successfully","access":str(access_token),"refresh":str(refresh)},status=200)
        except :
                return Response({"msg":"Something went worng in the Backend"},status=400)
        

@api_view(['POST'])
def login_user(request):
        try:
                data = request.data
                username = data.get('email')
                password = data.get('password')
                
                user = authenticate(username=username, password=password)
                if user:
                        refresh = RefreshToken.for_user(user)
                        access_token = refresh.access_token
                        return Response({'msg': 'Login successful !','access': str(access_token),'refresh': str(refresh),},status=200)
                else:
                        return Response({"msg": "Invalid credentials"}, status=400)
        except :
                return Response({"msg":"Something went worng in the Backend"},status=400)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_user_details(request):
        try:
                data=request.data
                user=request.user

                user.name=data.get('name',user.name)
                user.phone=data.get('phone',user.phone)
                user.profile_pic=data.get('profile_pic',user.profile_pic)
                user.save()
                return Response({"msg":"User Details Updated Successfully"},status=200)
        except :
                return Response({"msg":"Something went worng in the Backend"},status=400)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_details(request):
        user=request.user
        return Response({"data":{'username':user.name,'role':user.role,'profile_picture':user.profile_pic.url},'msg':'We Send You --> Name and Role'},status=200)