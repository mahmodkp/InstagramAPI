
from django.urls import path, include

from .views import FollowAPI, ProfileView, RegisterView, UpdateProfileView
# , UpdateProfileAPI, ProfileViewAPI
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r"register", RegisterView)
router.register(r"profile", ProfileView)
#router.register(r"updateprofile", UpdateProfileView)
urlpatterns = [
    path("", include(router.urls)),
    path('follow/<int:user_pk>/<int:followee_pk>', FollowAPI.as_view(), name='follow'),
    path('updateprofile/',
         UpdateProfileView.as_view(), name='updateprofile'),
    #path('profile/', ProfileView.as_view(), name='profile_view'),
]
