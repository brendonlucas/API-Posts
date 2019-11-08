from Posts.models import Post
from Posts.serializers import PostSerializer
from Profile.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from Profile.models import *
from rest_framework import status
import json
from Comment.models import *


@api_view(['GET', 'POST'])
def profile_list(request):
    if request.method == 'GET':
        # import_dados()
        profiles = Profile.objects.all()
        accounts_serializer = ProfileSerializer(profiles, many=True)
        return Response(accounts_serializer.data)

    elif request.method == 'POST':
        profiles_serializer = ProfileSerializer(data=request.data)
        if profiles_serializer.is_valid():
            profiles_serializer.save()
            return Response(profiles_serializer.data, status=status.HTTP_201_CREATED)
        return Response(profiles_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def profile_detail(request, id):
    try:
        profile = Profile.objects.get(id=id)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        profile_serializer = ProfileSerializer(profile)
        return Response(profile_serializer.data)

    elif request.method == 'PUT':
        profile_serializer = ProfileSerializer(Profile, data=request.data)
        if profile_serializer.is_valid():
            profile_serializer.save()
            return Response(profile_serializer.data)
        return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


@api_view(['GET', 'POST'])
def profile_post_list(request):
    if request.method == 'GET':
        profiles = Profile.objects.all()
        user_posts_serializer = ProfilePostSerializer(profiles, many=True)
        return Response(user_posts_serializer.data)


@api_view(['GET', 'POST'])
def profile_post_detail(request, id):
    try:
        profile = Profile.objects.get(id=id)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        profile_serializer = ProfilePostSerializer(profile)
        return Response(profile_serializer.data)
