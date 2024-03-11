from rest_framework import serializers

from .models import Media, Post, Comment, Hashtag
from accounts.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer class for article categories
    """
    # posts = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), many=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer class for article categories
    """
    likes = CustomUserSerializer(many=True)

    class Meta:
        model = Comment
        fields = '__all__'


class CommentWriteSerializer(serializers.ModelSerializer):
    """
    Serializer class for article categories
    """
    
    class Meta:
        model = Comment
        fields = ['post','content']
class HashtagSerializer(serializers.ModelSerializer):
    """
    Serializer class for article categories
    """
    # posts = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), many=True)

    class Meta:
        model = Hashtag
        fields = "__all__"


class MediaSerializer(serializers.ModelSerializer):
    """
    Serializer class for article categories
    """

    class Meta:
        model = Media
        fields = ['post','media','media_type']


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer class for article categories
    """
    comments = CommentSerializer(many=True)
    hashtags = HashtagSerializer(many=True)
    mentions = CustomUserSerializer(many=True)
    likes = CustomUserSerializer(many=True)
    media = MediaSerializer(many=True)
    # a=CustomUser.objects.get(pk=1)
    # a.set_password('123')

    class Meta:
        model = Post
        fields = ['id','caption', 'posted_time', 'location',
                  'comments', 'hashtags', 'mentions', 'likes', 'media']


class StorySerializer(serializers.ModelSerializer):
    """
    Serializer class for article categories
    """
    comments = CommentSerializer(many=True)
    hashtags = HashtagSerializer(many=True)
    mentions = CustomUserSerializer(many=True)
    likes = CustomUserSerializer(many=True)
    media = MediaSerializer(many=True)
    # a=CustomUser.objects.get(pk=1)
    # a.set_password('123')

    class Meta:
        model = Post
        fields = ['id', 'caption', 'posted_time', 'location',
                  'comments', 'hashtags', 'mentions', 'likes', 'media']


class PostWriteSerializer(serializers.ModelSerializer):
    """
    Serializer class for Post categories
    """
    # comments = CommentSerializer(many=True)
    # hashtags = HashtagSerializer(many=True)
    # mentions = CustomUserSerializer(many=True)
    # likes = CustomUserSerializer(many=True)
    # media = MediaSerializer(many=True)
    # a=CustomUser.objects.get(pk=1)
    # a.set_password('123')
    
    class Meta:
        model = Post
        fields = [
            'caption',
            'location',
        ]


# class BlogCommentSerializer(serializers.ModelSerializer):
#     """
#     Serializer class for get comments
#     """
#     user_name = serializers.CharField(
#         source="user.get_full_name", read_only=True)
#     read_only_fields = ('created_at',)

#     class Meta:
#         model = Comment
#         fields = ['user_name', 'text', 'created_at']


# class BlogMediaFileSerializer(serializers.ModelSerializer):
#     """
#     Serializer class for MediaFile model
#     """

#     class Meta:
#         model = MediaFile
#         fields = '__all__'


# class BlogCommentWriteSerializer(serializers.ModelSerializer):
#     """
#     Serializer class for create and update comments
#     """
#     user_name = serializers.CharField(
#         source="user.get_full_name", read_only=True)

#     class Meta:
#         model = Comment
#         fields = ['user_name', 'article', 'text']

#     def create(self, validated_data):
#         user = self.context['user']
#         return Comment.objects.create(user=user, **validated_data)


# class ArticleSerializer(serializers.ModelSerializer):
#     """
#     Serializer class for reading Articles
#     """

#     category = serializers.CharField(source="category.name", read_only=True)

#     class Meta:
#         model = Article
#         fields = '__all__'
