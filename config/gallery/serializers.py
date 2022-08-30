from rest_framework import serializers
from django.contrib.auth.models import User

from gallery.models import Gallery

class CreateGalleryUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('profile_photo',)

class GalleryREADSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="to_user.username")
    class Meta:
        model = Gallery
        fields = ('pk', 'username' ,'profile_photo',)

class GalleryToUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('pk', 'profile_photo',)

class GalleryRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('pk', 'profile_photo', 'changed', 'created')

class UserREADSerializer(serializers.ModelSerializer):
    photos = GalleryToUserSerializer(source="photo", many=True)
    class Meta:
        model = User
        fields = ('pk', 'username', 'first_name', 'last_name', 'email', 'photos',)

class UserCREATESerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('pk', 'username', 'first_name', 'last_name', 'email', 'password')
    
    def create(self, validated_data):
        model = self.Meta.model
        user = model.objects.create_user(**validated_data)
        return user
        