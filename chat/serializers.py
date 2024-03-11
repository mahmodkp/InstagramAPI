from rest_framework import serializers
from .models import DirectMessage


class MessageSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = DirectMessage
        fields = '__all__'
