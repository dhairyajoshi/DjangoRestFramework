from rest_framework import serializers
from .models import Post
from .models import Notification

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Post
        fields='__all__'


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model= Notification
        fields= '__all__'