from django.contrib.auth.models import User
from rest_framework import serializers
from Comment.models import *
from Posts.models import Post


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'email', 'body']


class PostCommentsSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True)

    class Meta:
        model = Post
        fields = ['userId', 'title', 'body', 'comments']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    games = PostCommentsSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'pk', 'username', 'games')
