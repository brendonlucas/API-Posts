from django.contrib.auth.models import User
from rest_framework import serializers
from Comment.models import *
from Posts.models import Post, Profile


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'email', 'body']


class PostCommentsSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True)

    class Meta:
        model = Post
        fields = ['profile', 'title', 'body', 'comments']


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'pk', 'username')


class ProfileSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['name']

class PostSerializers(serializers.ModelSerializer):
    profile = ProfileSerializers()

    class Meta:
        model = Post
        fields = [ 'profile', 'id', 'title', 'body']
