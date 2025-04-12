from rest_framework import ModelSerializer, serializers
from django.contrib.auth.models import User
from .models import Book


class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )    
        return user


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class BookSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'age', 'genre', 'user']
        read_only_fields = ['user']