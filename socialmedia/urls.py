"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from hashtags.views import HashTagView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_registration.urls')),
    path('post/', include('posts.urls',namespace='post')),
    path('tags/<hashtag>/', HashTagView.as_view(),name='post-hashtags'),
    path('api-auth/', include('rest_framework.urls')),
    path('post/api/', include('posts.api.urls',namespace='post-api')),
    path('profile/api/', include('user_registration.api.urls',namespace='user-api')),
    path('tags/<hashtag>/api/', include('hashtags.api.urls',namespace='hashtag-api'))
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)