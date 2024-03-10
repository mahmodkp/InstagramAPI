from .serializers import UserRegisterSerializer
from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django.contrib.auth import get_user_model
from rest_framework.views import APIView

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
        except folowee.DoesNotExist:
            folowee = None
        if user is not None and folowee is not None:
            if user in folowee.following.all():
                folowee.following.remove(user)
                folowee.save()
                print('remove')
            else:
                folowee.following.add(user)
                folowee.save()
                print('added')
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
                        data={"error": "Invalid pk values"})

class ProfileView(viewsets.ViewSet):
    
    pass


class RegisterView(viewsets.ModelViewSet):
    http_method_names = [
        'post','Put'
    ]
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    
