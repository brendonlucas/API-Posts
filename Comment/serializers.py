from rest_framework import serializers
from Comment.models import Comment
from Posts.models import Post


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'email', 'body']


class CommentsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class PostCommentsSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True)

    class Meta:
        model = Post
        fields = ['comments']
