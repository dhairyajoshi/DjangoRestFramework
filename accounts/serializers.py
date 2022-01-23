from rest_framework import serializers
from .models import NewUser


class CustomUserSerializer(serializers.ModelSerializer):


    class Meta:
        model = NewUser
        fields = ('username', 'first_name', 'bio', 'pfp','cfp', 'password', 'posts', 'likes','is_staff')
        extra_kwargs = {'password': {'write_only': True}} 

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance 
