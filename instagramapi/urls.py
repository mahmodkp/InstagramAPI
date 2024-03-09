"""
URL configuration for instagramapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
schema_view = get_schema_view(
    openapi.Info(
        title="Instagram Clone",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path(f'{settings.ADMIN_URL}/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    #re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^auth/', include('djoser.urls')),
    # re_path(r'^auth/', include('djoser.urls.authtoken')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
    re_path(r'^auth/', include('djoser.social.urls')),
    path('upload/', include('drf_file_upload.urls')),
    # App Routes
    path("api/v1/contents/", include('content.urls')),
    # path("api/v1/blog/", include('blog.urls')),
    # path("api/v1/orders/", include('orders.urls')),
    # path("api/v1/payments/", include('payments.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
