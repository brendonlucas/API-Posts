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
        endereco = validated_data.get('address')
        street = endereco['street']
        suite = endereco['suite']
        city = endereco['city']
        zipcode = endereco['zipcode']
        a = Address(street=street, suite=suite, city=city, zipcode=zipcode)
        a.save()
        user = User.objects.create_user(username=name, password='123456789', email=email)
        p = Profile(name=name, email=email, address=a, user_complement=user)
        p.save()

        return validated_data

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address')
        address = instance.address
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)

        address.street = address_data.get('street', address.street)
        address.suite = address_data.get('suite', address.suite)
        address.city = address_data.get('city', address.city)
        address.zipcode = address_data.get('zipcode', address.zipcode)

        instance.save()
        address.save()
        return instance




