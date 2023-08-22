from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Like, UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserProfile()

    class Meta:
        model = User
        fields = '__all__'