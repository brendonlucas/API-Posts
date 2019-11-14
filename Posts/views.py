from rest_framework import serializers, generics, permissions
from Posts.models import Post
from Posts.permissions import IsOwnerOrReadOnly
from Posts.serializers import *


class PostCommentslist(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCommentsSerializer
    name = 'post-comments-list'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,)


class PostCommentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCommentsSerializer
    name = 'post-comments-detail'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
