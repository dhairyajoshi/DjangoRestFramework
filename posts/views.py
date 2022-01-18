from cgi import parse_multipart
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import NotificationSerializer, PostSerializer
from .models import Notification, Post

# Create your views here.


@api_view(['GET'])
def getposts(request):
    if not request.user.is_authenticated:
        return Response({'error':'user not authenticated'})

    data= Post.objects.all()

    print(data)

    serialized = PostSerializer(data,many=True)

    return Response(serialized.data)


@api_view(['GET'])
def getpost(request,id):
    if not request.user.is_authenticated:
        return Response({'error':'user not authenticated'})
    data= Post.objects.get(id=id)

    serialized = PostSerializer(data,many=False)

    return Response(serialized.data)


@api_view(['POST'])
def addpost(request):
    if not request.user.is_authenticated:
        return Response({'error':'user not authenticated'})
    serialized = PostSerializer(data=request.data)

    if serialized.is_valid():
        serialized.save(username= request.user.username,user=request.user)

    return Response(serialized.data)


@api_view(['POST'])
def likepost(request,id):
    if not request.user.is_authenticated:
        return Response({'error':'user not authenticated'})
    post = Post.objects.get(id=id)
    post.likes= post.likes+1
    sender=request.user

    notification = Notification.objects.create(
        sender=sender.username,
        receiver=post.username,
        post=post.caption, 
        pic=post.pic

    )
 
    serialized=NotificationSerializer(data=notification)

    if serialized.is_valid(): 
        serialized.save()
    else:
        print(serialized.error_messages) 

    post.save() 

    res={"msg":"post likes updated!"}
    return Response(res)


