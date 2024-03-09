from content.views import (
                        # CreatePostAPI,
                        GetPostAPI,
                        UpdatePostAPI,
                        DeletePostAPI,
                        #LikePostAPI,
                        # SavePostAPI
                        )
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
   HashtagViewset,
   LikePostAPI,
   MediaViewset,
   PostViewset,
)

app_name = "Post"
router = DefaultRouter()
#router.register(r"post", PostViewset)
#router.register(r"hashtag", HashtagViewset)
router.register(r"media", MediaViewset)
# router.register(r"categories", CategoryViewSet)
# router.register(r"comments", CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
    
    path('post/get/<int:pk>/',
         GetPostAPI.as_view(),
         name='create_post_api'),

    path('post/update/<int:pk>/',
         UpdatePostAPI.as_view(),
         name='create_post_api'),

    path('post/delete/<int:pk>/',
         DeletePostAPI.as_view(),
         name='create_post_api'),
    
    path('post/like/<int:user_pk>/<int:post_pk>/',
         LikePostAPI.as_view(),
         name='create_post_api'),

    

]   
