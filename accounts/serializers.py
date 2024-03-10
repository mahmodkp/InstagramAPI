from rest_framework import serializers


from accounts.models import CustomUser


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    Serializer class for article categories
    """
    # posts = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), many=True)

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "mobile",
            "bio",
            "birthday",
            "gender",
        ]
