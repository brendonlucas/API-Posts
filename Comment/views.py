from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Comment.models import Comment
from Comment.serializers import *
from Posts.models import Post, Profile
from Posts.permissions import IsOwnerOrReadOnly


class CommentsPostlist(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    name = 'comments-post-list'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


@api_view(['GET', 'POST'])
def commentslist(request, id_post):
    print('entou')
    try:
        post = Post.objects.get(id=id_post)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        comment_serializer = PostCommentsSerializer(post)
        return Response(comment_serializer.data)

    elif request.method == 'POST':
        if request.user.is_authenticated:
            comment_serializer = CommentsSerializer(Comment, data=request.data)
            if comment_serializer.is_valid():
                comment = Comment(name=request.data['name'], email=request.data['email'], body=request.data['body'],
                                  postId=post)
                comment.save()
                return Response(request.data)
            return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', 'PUT', 'DELETE'])
def comments_post_detail(request, id_post, id_comment):
    try:
        comment = Comment.objects.filter(postId=id_post)
        if id_comment <= len(comment):
            comment = comment[id_comment - 1]
        else:
            return Response({'erro': '404_NOT_FOUND'}, status=status.HTTP_404_NOT_FOUND)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        comment_serializer = CommentsSerializer(comment)
        return Response(comment_serializer.data)

    elif request.method == 'PUT':
        comment_serializer = CommentsUpdateSerializer(Comment, data=request.data)
        if comment_serializer.is_valid():
            comment.name = request.data['name']
            comment.email = request.data['email']
            comment.body = request.data['body']
            comment.save()
            return Response(request.data)
        return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user = request.user
        post = Post.objects.get(id=id_post)
        if post.owner == user:
            comment.delete()
            return Response({'result': 'comment deleted'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'Você não tem autorização para deletar o comentario'}, status=status.HTTP_401_UNAUTHORIZED)




