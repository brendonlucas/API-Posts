from rest_framework.decorators import api_view

from Posts.views import *
from rest_framework.reverse import reverse
from rest_framework.response import Response
from Profile.serializers import *
from Profile.models import *
from rest_framework import status
from rest_framework import serializers, generics
import json
from rest_framework.views import APIView


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-list'


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-detail'


class ProfilePostlist(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerializer
    name = 'profile-post-list'


class ProfilePostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerializer
    name = 'profile-post-detail'


@api_view(['GET'])
def info(request):
    if request.method == 'GET':
        lista = []
        profiles = Profile.objects.all()
        for i in range(len(profiles)):
            num_id = profiles[i].id
            name = profiles[i].name
            total_posts = len(Post.objects.filter(userId=num_id))
            total_coments = len(Comment.objects.filter(postId__userId=num_id))
            dic = {'id': num_id, 'name': name, 'total_posts': total_posts, 'total_coments': total_coments}
            lista.append(dic)
        return Response(lista)


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'profile-list': reverse(ProfileList.name, request=request),
            'profile-post-list': reverse(ProfilePostlist.name, request=request),
            'post-comments-list': reverse(PostCommentslist.name, request=request),
            'info': reverse('info', request=request)
        }, status=status.HTTP_200_OK)


def import_dados():
    conteudo = open('db.json').read()
    lista = json.loads(conteudo)

    for j in range(len(lista['users'])):
        n_id = lista['users'][j]['id']
        name = lista['users'][j]['name']
        email = lista['users'][j]['email']
        endereco = lista['users'][j]['address']
        street = endereco['street']
        suite = endereco['suite']
        city = endereco['city']
        zipcode = endereco['zipcode']
        # a = Address(street=street, suite=suite, city=city, zipcode=zipcode)
        # a.save()
        # p = Profile(name=name, email=email, address=a)
        # p.save()

    for i in range(len(lista['posts'])):
        # user = Profile.objects.get(id=lista['posts'][i]['userId'])
        titulo = lista['posts'][i]['title']
        body = lista['posts'][i]['body']
        # Post(title=titulo, body=body, userId=user).save()

    for k in range(len(lista['comments'])):
        # post_id = Post.objects.get(id=lista['comments'][k]['postId'])
        name = lista['comments'][k]['name']
        email = lista['comments'][k]['email']
        body = lista['comments'][k]['body']
        # Comment(name=name, email=email, body=body, postId=post_id).save()
