from rest_framework import generics, mixins
from .serializers import UserReadSerializer, UserWriteSerializer
from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.generics import (  # CreateAPIView,
    # ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView)

User = get_user_model()


class FollowAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            user = get_user_model().objects.get(pk=kwargs['user_pk'])
        except get_user_model().DoesNotExist:
            user = None
        if user:
            if user.id != request.user.id:
                return Response(status=status.HTTP_403_FORBIDDEN)
        try:
            folowee = User.objects.get(pk=kwargs['followee_pk'])
        except User.DoesNotExist:
            folowee = None
        if user is not None and folowee is not None:
            if user in folowee.followers.all():
                folowee.followers.remove(user)
                user.following.remove(folowee)
                folowee.save()
                user.save()
                print('remove')
            else:
                folowee.followers.add(user)
                user.following.add(folowee)
                folowee.save()
                user.save()
                print('added')
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
                        data={"error": "Invalid pk values"})


class ProfileView(mixins.ListModelMixin,
                  GenericViewSet):
    serializer_class = UserReadSerializer
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        
        user = self.request.user
        if not user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        user.password = ''
        serializer = UserReadSerializer(user)
        return Response(serializer.data)


class RegisterView(viewsets.ModelViewSet):
    http_method_names = [
        'post',
    ]
    queryset = User.objects.all()
    serializer_class = UserWriteSerializer


class UpdateProfileView(UpdateAPIView):
    # http_method_names = [
    #     'put',
    # ]
    queryset = User.objects.all()
    serializer_class = UserWriteSerializer
    def put(self, request, *args, **kwargs):
        instance = self.request.user
        if not instance:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)