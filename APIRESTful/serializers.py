from rest_framework.serializers import ModelSerializer, ValidationError
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from . import models


class UserSerializer(ModelSerializer):
	email = serializers.EmailField(
		required=True, 
		validators=[UniqueValidator(queryset=models.User.objects.all())]
	)
	password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
	password2 = serializers.CharField(write_only=True, required=True)

	class Meta:
		model = models.User
		fields = ('username', 'email', 'password', 'password2')

	def validate(self, attrs):
		if attrs['password'] != attrs['password2']:
			raise serializers.ValidationError({"password":"Password fields didn't match."})
		return attrs

	def create(self, validated_data):
		user = models.User.objects.create(
			username=validated_data['username'],
			email=validated_data['email']
		)
		user.set_password(validated_data['password'])
		user.save()
		return user


class PhotoSerializer(ModelSerializer):
	class Meta:
		model = models.Photo
		fields = ('id', 'name', 'image', 'uploader', 'date_created')


class PhotoSerializer(ModelSerializer):
	class Meta:
		model = models.Photo
		fields = ('id', 'name', 'image', 'uploader', 'date_created')


class ClubSerializer(ModelSerializer):
	class Meta:
		model = models.Photo
		fields = ('id', 'name', 'address', 'photo', 'presentation', 'infrastructure',
            'secretariat', 'network_link', 'network_link_2')
        

class EventSerializer(ModelSerializer):
	class Meta:
		model = models.Event
		fields = ('id', 'title', 'description', 'date', 'address', 'photo', 'date_created')


class CategorySerializer(ModelSerializer):
	class Meta:
		model = models.Category
		fields = ('id', 'category_choices')


class LevelSerializer(ModelSerializer):
	class Meta:
		model = models.Level
		fields = ('id', 'level_choice')


class TeamSerializer(ModelSerializer):
	class Meta:
		model = models.Team
		fields = ('id', 'category', 'level', 'coach', 'coach_adj', 'photo', 'classement', 'agenda')