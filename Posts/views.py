from rest_framework import serializers, generics
from Posts.models import Post
from Posts.serializers import *


class PostCommentslist(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCommentsSerializer
    name = 'post-comments-list'


class PostCommentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCommentsSerializer
    name = 'post-comments-detail'
