from rest_framework import serializers


from accounts.models import CustomUser


class UserWriteSerializer(serializers.ModelSerializer):
    """
    Serializer class for user registration
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

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            mobile=validated_data['mobile'],
            bio=validated_data['bio'],
            birthday=validated_data['birthday'],
            gender=validated_data['gender'],
            
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        # instance.username=validated_data['username'],
        # instance.email=validated_data['email'],
        # instance.first_name=validated_data['first_name'],
        # instance.last_name=validated_data['last_name'],
        # instance.mobile=validated_data['mobile'],
        # instance.bio=validated_data['bio'],
        # instance.birthday=validated_data['birthday'],
        # instance.gender=validated_data['gender'],
        instance.set_password(validated_data['password'])
        return super().update(instance, validated_data)
        # instance.save()
        # return instance
    


class UserReadSerializer(serializers.ModelSerializer):
    """
    Serializer class for user 
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

    
