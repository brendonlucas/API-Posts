from rest_framework import serializers

from Posts.models import Post
from Profile.models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body')


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('street', 'suite', 'city', 'zipcode')


class ProfilePostSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    address = AddressSerializer()

    class Meta:
        model = Profile
        fields = ('id', 'name', 'email', 'address', 'posts')


class ProfileSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Profile
        fields = ('id', 'name', 'email', 'address')

    def create(self, validated_data):
        name = validated_data.get('name')
        email = validated_data.get('email')
        p = Profile(name=name, email=email)

        endereco = validated_data.get('address')
        street = endereco['street']
        suite = endereco['suite']
        city = endereco['city']
        zipcode = endereco['zipcode']
        p.save()
        a = Address(street=street, suite=suite, city=city, zipcode=zipcode, user=p)
        a.save()
        return validated_data
