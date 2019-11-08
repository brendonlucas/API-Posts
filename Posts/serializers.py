from rest_framework import serializers
from Posts.models import Post, Profile
from Profile.serializers import ProfileSerializer
from rest_framework import serializers

from Posts.models import Post
from Profile.models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = 'street', 'suite', 'city', 'zipcode'


class ProfilePostSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)
    address = AddressSerializer(many=True)

    class Meta:
        model = Profile
        fields = ['id', 'name', 'email', 'address', 'posts']
