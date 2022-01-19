import email
import re
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import NewUser
from .serializers import CustomUserSerializer
from posts.serializers import NotificationSerializer
from posts.models import Notification
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

@api_view(['POST'])
def updatePic(request):
    if not request.user.is_authenticated:
        return Response({'error':'user not authenticated'})

    user= NewUser.objects.get(id=request.user.id)

    data= request.data
    
    user.pfp=data['pfp']

    user.save()

    serialized= CustomUserSerializer(user)

    return Response(serialized.data)  

    
  

@api_view(['POST'])
def registerUser(request):  
    serialized= CustomUserSerializer(data=request.data)
    data={}
    if serialized.is_valid():
        instance=serialized.save() 
        refresh = RefreshToken.for_user(instance)
        data['user']=serialized.data
        data['token']=str(refresh.access_token)


    return Response(data)

@api_view(['POST'])
def loginUser(request):  
    
    data={}
    reqdata= request.data
    username=reqdata['username']
    password=reqdata['password']

    user = NewUser.objects.get(username=username)
    serialized= CustomUserSerializer(user)

    if user.check_password(password):
        refresh = RefreshToken.for_user(user)
        data['user']=serialized.data
        data['token']=str(refresh.access_token) 
    
    else: 
        data['error']='wrong credentials'
    

    return Response(data)

  
@api_view(['GET'])
def getnotifs(request):
    if not request.user.is_authenticated:
        return Response({'error':'user not authenticated'})

    data= Notification.objects.filter(receiver=request.user.username)

    serialized = NotificationSerializer(data,many=True)

    response=serialized.data

    data.delete()

    return Response(response)

@api_view(['GET'])
def getinfo(request):
    if not request.user.is_authenticated:
        return Response({'error':'user not authenticated'})

    data= NewUser.objects.get(username=request.user.username)

    serialized = CustomUserSerializer(data,many=False)

    return Response(serialized.data)

    