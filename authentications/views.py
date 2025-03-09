from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from .models import CustomUser
from .permissions import IsSeller
from rest_framework_simplejwt.tokens import RefreshToken

DEFAULT_PROFILE_PIC_URL = 'https://www.pngfind.com/pngs/m/292-2924933_image-result-for-png-file-user-icon-black.png'

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
                        return Response({'ofBackendMessage': 'Email already exists'}, status=400)
                
                user = CustomUser.objects.create_user(username=username, password=password, email=email,role=role,name=name,phone=phone,profile_pic=profile_pic)
                user.save()
                refresh = RefreshToken.for_user(user)
                access_token = refresh.access_token
                return Response({"ofBackendMessage":"Account Created Successfully","access":str(access_token),"refresh":str(refresh)},status=200)
        except :
                return Response({"ofBackendMessage":"Something went worng in the Backend"},status=400)
        

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
                        return Response({'ofBackendMessage': 'Login successful !','access': str(access_token),'refresh': str(refresh),},status=200)
                else:
                        return Response({"ofBackendMessage": "Invalid credentials"}, status=400)
        except :
                return Response({"ofBackendMessage":"Something went worng in the Backend"},status=400)
        
@api_view(['POST'])
def refresh_token(request):
        try:
                data = request.data
                refresh = data.get('refresh')
                token = RefreshToken(refresh)
                access = str(token.access_token)
                return Response({ 'access': str(access)})
        except :
                return Response({"ofBackendMessage":"Something went worng in the Backend"},status=400)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_user_details(request):
        try:
                data=request.data
                user=request.user

                user.name=data.get('name',user.name)
                user.phone=data.get('phone',user.phone)
                user.email=data.get('email',user.email)
                user.profile_pic=data.get('profile_pic',user.profile_pic)
                user.save()
                return Response({"ofBackendMessage":"User Details Updated Successfully !"},status=200)
        except :
                return Response({"ofBackendMessage":"Something went worng in the Backend"},status=400)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_details(request):
        user=request.user
        #Using ternary operator to check if the user has profile pic or not : value_if_true if condition else value_if_false
        profile_pic_url = user.profile_pic.url if user.profile_pic else DEFAULT_PROFILE_PIC_URL    #return the user details
        user_details={
                
                'name':user.name,
                'role':user.role,
                'email':user.email,
                'phone':user.phone,
                'profile_picture':profile_pic_url
        }
        return Response({"ofBackendData":user_details,'ofMessage':'We Send You --> Name and Role'},status=200)