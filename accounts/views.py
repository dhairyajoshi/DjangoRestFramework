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
from posts.models import Post
# Create your views here.
    
@api_view(['POST'])
def updateProfile(request):
    if not request.user.is_authenticated:
        return Response({'error':'user not authenticated'})

    user= NewUser.objects.get(id=request.user.id)

    data= request.data
    first_name=data['first_name']
    bio= data['bio']
    
    user.first_name=first_name
    user.bio=bio

    user.save()

    return Response({'msg':'Updated successfully'})  
   
@api_view(['POST'])
def updatePfp(request):
    if not request.user.is_authenticated:
        return Response({'error':'user not authenticated'})

    user= NewUser.objects.get(id=request.user.id)

    data= request.data
    user.pfp=data['pfp']

    serialized=CustomUserSerializer(user)

    userposts= Post.objects.filter(user=request.user)

    for u in userposts:
        u.pfp=user.pfp
        u.save()
    

    user.save()
    

    return Response(serialized.data)  

@api_view(['POST'])
def updateCfp(request):
    if not request.user.is_authenticated:
        return Response({'error':'user not authenticated'})

    user= NewUser.objects.get(id=request.user.id)

    data= request.data
    user.cfp=data['cfp']
    
    serialized=CustomUserSerializer(user)
    user.save()

    return Response(serialized.data)  

    
@api_view(['POST'])
def registerUser(request):  
    serialized= CustomUserSerializer(data=request.data)
    data={}
    if serialized.is_valid():
        instance=serialized.save() 
        refresh = RefreshToken.for_user(instance)
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
        # data['user']=serialized.data
        data['token']=str(refresh.access_token) 
    
    else: 
        data['error']='wrong credentials'
    

    return Response(data)

  
@api_view(['GET'])
def getnotifs(request):
    if not request.user.is_authenticated:
        return Response({'error':'user not authenticated'})

    data= Notification.objects.filter(receiver=request.user.username).exclude(sender=request.user).order_by('-date')

    serialized = NotificationSerializer(data,many=True)

    response=serialized.data


    return Response(response)

@api_view(['GET'])
def getinfo(request):
    if not request.user.is_authenticated:
        return Response({'error':'user not authenticated'})

    data= NewUser.objects.get(username=request.user.username)

    serialized = CustomUserSerializer(data,many=False)

    return Response(serialized.data)

    
@api_view(['GET'])
def getinfoUsr(request,usr):
    if not request.user.is_authenticated:
        return Response({'error':'user not authenticated'})

    data= NewUser.objects.get(username=usr)

    serialized = CustomUserSerializer(data,many=False)

    return Response(serialized.data)