from rest_framework import serializers, generics, permissions
from Posts.models import Post
from Posts.permissions import IsOwnerOrReadOnly
from Posts.serializers import *
from Profile.models import Profile


class Postlist(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    name = 'post-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    name = 'post-list'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


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
