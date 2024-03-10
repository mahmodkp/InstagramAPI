from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import (
    CommentSerializer,
    CommentWriteSerializer,
    HashtagSerializer,
    MediaSerializer,
    PostSerializer,
    CustomUserSerializer,
    PostWriteSerializer,
)
from django.contrib.auth import get_user_model
from rest_framework.views import APIView

from rest_framework.decorators import action
from rest_framework import status
from .models import Comment, Hashtag, Media, Post
from rest_framework.generics import (  # CreateAPIView,
    # ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView)


class PostViewset(viewsets.ModelViewSet):
    """
    List and Retrieve article categories
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = PostWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.request.user
        caption = serializer.validated_data.get("caption")
        location = serializer.validated_data.get("location")
        Post.objects.create(author=user, caption=caption, location=location)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['GET'])
    def comments(self, request, pk=None):
        post = self.get_object()
        serializer = CommentSerializer(post.Comment_from_Post, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def likes(self, request, pk=None):
        post = self.get_object()
        serializer = CustomUserSerializer(post.likes, many=True)
        return Response(serializer.data)

    # def get_serializer(self):
    #     if self.action in ("create", "update", "partial_update", "destroy"):
    #         return PostWriteSerializer
    #     return PostSerializer

    # @action(detail=True, methods=['GET', 'POST'])
    # def likes(self, request, pk=None):
    #     post = self.get_object()  # Post.objects.filter(id=pk).first()
    #     serializer = CustomUserSerializer(post.likes, many=True)
    #     return Response(serializer.data)


class CommentView(viewsets.ModelViewSet):
    http_method_names = ['post', 'put']
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = CommentWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.request.user
        content = serializer.validated_data.get("content")
        post = serializer.validated_data.get("post")
        Comment.objects.create(author=user, content=content, post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MediaView(viewsets.ModelViewSet):
    http_method_names = ['post', 'put']
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = MediaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        media = serializer.validated_data.get("media")
        media_type = serializer.validated_data.get("media_type")
        post = serializer.validated_data.get("post")
        Media.objects.create(post=post, media=media, media_type=media_type)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# class CreatePostAPI(APIView):
#     def post(self, request, *args, **kwargs):
#         data = request.data
#         usertags = []
#         hashtags = []
#         for usertag_pk in data.get('usertags'):
#             try:
#                 usertag = get_user_model().objects.get(pk=usertag_pk)
#             except get_user_model().DoesNotExist:
#                 usertag = None
#             if usertag is not None:
#                 usertags.append(usertag)
#         for hashtag_pk in data.get('hashtags'):
#             try:
#                 hashtag = get_user_model().objects.get(pk=hashtag_pk)
#             except get_user_model().DoesNotExist:
#                 hashtag = None
#             if hashtag is not None:
#                 hashtags.append(hashtag)
#         try:
#             author = get_user_model().objects.get(pk=data.get('author'))
#         except get_user_model().DoesNotExist:
#             author = None
#         if author is not None:
#             post = Post(
#                 author=author,
#                 image=request.FILES["image"],
#                 caption=data.get('caption'),
#                 location=data.get('location'),
#                 usertags=usertags,
#                 hashtags=hashtags,
#             )
#             post.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_404_NOT_FOUND,
#                         data={"error": "Invalid pk values"})


class MediaViewset(viewsets.ModelViewSet):
    """
    List and Retrieve article categories
    """

    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes = (permissions.AllowAny,)


class HashtagViewset(viewsets.ModelViewSet):
    """
    List and Retrieve article categories
    """
    http_method_names = ['get', 'post', 'put']
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
    permission_classes = (permissions.AllowAny,)


class GetPostAPI(RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class UpdatePostAPI(UpdateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class DeletePostAPI(DestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class LikePostAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            user = get_user_model().objects.get(pk=kwargs['user_pk'])
        except get_user_model().DoesNotExist:
            user = None
        # if user:
        #     if user.id != request.user.id:
        #         return Response(status=status.HTTP_403_FORBIDDEN)
        try:
            post = Post.objects.get(pk=kwargs['post_pk'])
        except Post.DoesNotExist:
            post = None
        if user is not None and post is not None:
            if user in post.likes.all():
                post.likes.remove(user)
                post.save()
                print('added')
            else:
                post.likes.add(user)
                post.save()
                print('remove')
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
                        data={"error": "Invalid pk values"})
