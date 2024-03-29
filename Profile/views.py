from datetime import date, timedelta
from datetime import datetime
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import obtain_auth_token, ObtainAuthToken
from rest_framework.decorators import api_view
from rest_framework.throttling import ScopedRateThrottle

from Posts.permissions import IsOwnerUserOrReadOnly
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
    permission_classes = (
        permissions.IsAuthenticated,)


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-detail'
    permission_classes = (
        permissions.IsAuthenticated, IsOwnerUserOrReadOnly,)


class ProfilePostlist(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerializer
    name = 'profile-post-list'


class ProfilePostDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerializer
    name = 'profile-post-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,)


@api_view(['GET'])
def info(request):
    if request.method == 'GET':
        lista = []
        profiles = Profile.objects.all()
        for i in range(len(profiles)):
            num_id = profiles[i].id
            name = profiles[i].name
            total_posts = len(Post.objects.filter(profile=num_id))
            total_coments = len(Comment.objects.filter(postId__profile=num_id))
            dic = {'id': num_id, 'name': name, 'total_posts': total_posts, 'total_coments': total_coments}
            lista.append(dic)
        return Response(lista)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    permission_classes = (
        permissions.IsAuthenticated,)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
    permission_classes = (
        permissions.IsAuthenticated,)


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'profile-list': reverse(ProfileList.name, request=request),
            'post-list': reverse(Postlist.name, request=request),
            'profile-post-list': reverse(ProfilePostlist.name, request=request),
            'post-comments-list': reverse(PostCommentslist.name, request=request),
            'users': reverse(UserList.name, request=request),
            'info': reverse('info', request=request),
            'get-Token': reverse('get-token', request=request),
            'import-dados': reverse('import-dados', request=request),

        }, status=status.HTTP_200_OK)


@api_view(['GET'])
def import_dados(request):
    if request.method == 'GET':
        conteudo = open('db.json').read()
        lista = json.loads(conteudo)
        for j in range(len(lista['users'])):
            username = lista['users'][j]['username']
            name = lista['users'][j]['name']
            email = lista['users'][j]['email']
            endereco = lista['users'][j]['address']
            street = endereco['street']
            suite = endereco['suite']
            city = endereco['city']
            zipcode = endereco['zipcode']
            a = Address(street=street, suite=suite, city=city, zipcode=zipcode)
            a.save()
            user = User.objects.create_user(username=username, password='123456789', email=email)
            p = Profile(name=name, email=email, address=a, user_complement=user)
            p.save()

        for i in range(len(lista['posts'])):
            user = Profile.objects.get(id=lista['posts'][i]['userId'])
            owner = user.user_complement
            titulo = lista['posts'][i]['title']
            body = lista['posts'][i]['body']
            Post(title=titulo, body=body, profile=user, owner=owner).save()

        for k in range(len(lista['comments'])):
            post_id = Post.objects.get(id=lista['comments'][k]['postId'])
            name = lista['comments'][k]['name']
            email = lista['comments'][k]['email']
            body = lista['comments'][k]['body']
            Comment(name=name, email=email, body=body, postId=post_id).save()
        return Response({'Importado com sucesso'}, status=status.HTTP_200_OK)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
    throttle_scope = 'get-token'
    throttle_classes = (ScopedRateThrottle,)
