from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from datetime import datetime
from . import models, serializers


class UserViewset(ModelViewSet):
    #permission_classes = [IsAuthenticated]
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        return models.User.objects.all()


class PhotoViewset(ModelViewSet):
    #permission_classes = [IsAuthenticated]
    serializer_class = serializers.PhotoSerializer

    def get_queryset(self):
        return models.Photo.objects.all()


class ClubViewset(ModelViewSet):
    #permission_classes = [IsAuthenticated]
    serializer_class = serializers.ClubSerializer

    def get_queryset(self):
        return models.Club.objects.all()


class EventViewset(ModelViewSet):
    #permission_classes = [IsAuthenticated]
    serializer_class = serializers.EventSerializer

    def get_queryset(self):
        return models.Event.objects.all()


class CategoryViewset(ModelViewSet):
    #permission_classes = [IsAuthenticated]
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        return models.Category.objects.all()


class LevelViewset(ModelViewSet):
    #permission_classes = [IsAuthenticated]
    serializer_class = serializers.LevelSerializer

    def get_queryset(self):
        return models.Level.objects.all()


class TeamViewset(ModelViewSet):
    #permission_classes = [IsAuthenticated]
    serializer_class = serializers.TeamSerializer

    def get_queryset(self):
        return models.Team.objects.all()
