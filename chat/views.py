from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import DirectMessageSerializer
from .models import DirectMessage
from rest_framework.response import Response
from rest_framework import status

class CreateMessage(CreateAPIView):
    serializer_class = DirectMessageSerializer
    permission_classes = (IsAuthenticated,)
    queryset = DirectMessage.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = DirectMessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.request.user
        sender = serializer.validated_data.get("sender")
        if sender.id != self.request.user.id:
            return Response(serializer.data, status=status.HTTP_403_FORBIDDEN)
        return self.create(request, *args, **kwargs)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        


class RetrieveMessage(RetrieveAPIView):
    serializer_class = DirectMessageSerializer
    permission_classes = (IsAuthenticated,)
    queryset = DirectMessage.objects.all()