from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'first_name', 'last_name', 'bio', 'image', 'date_joined']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name']

class ListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listing
        # fields = ['id', 'user', 'title', 'description', 'price', 'quantity', 'image', 'created_at']
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        # fields = ['id', 'sender', 'reciever', 'content', 'timestamp', 'image']
        fields = '__all__'

