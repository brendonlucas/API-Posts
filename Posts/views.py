from rest_framework.decorators import api_view
from rest_framework.response import Response

from Posts.models import Post
from Posts.serializers import *


@api_view(['GET', 'POST'])
def profile_post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        user_posts_serializer = ProfilePostSerializer(posts, many=True)
        return Response(user_posts_serializer.data)
