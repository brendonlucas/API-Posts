from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Comment.models import Comment
from Comment.serializers import *
from Posts.models import Post


class CommentsPostlist(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCommentsSerializer
    name = 'comments-post-list'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def comments_post_detail(request, id_post, id_comment):
    try:
        comment = Comment.objects.filter(postId=id_post)
        if id_comment <= len(comment):
            comment = comment[id_comment - 1]
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        comment_serializer = CommentsSerializer(comment)
        return Response(comment_serializer.data)

    elif request.method == 'PUT':
        comment_serializer = CommentsUpdateSerializer(Comment, data=request.data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(request.data)
        return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
