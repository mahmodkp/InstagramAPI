from django.urls import path
from .views import MessageView, RetrieveMessageView

urlpatterns = [
    path('message/', MessageView.as_view(), name='send-message'),
    path('message/<int:pk>/', RetrieveMessageView.as_view(), name='get-message'),
]
