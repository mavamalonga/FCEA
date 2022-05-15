from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static
from APIRESTful import views
from accueil.views import *


router = routers.SimpleRouter()
router.register('user', views.UserViewset, basename='user')
router.register('club', views.ClubViewset, basename='club')
router.register('event', views.EventViewset, basename='event')
router.register('team', views.TeamViewset, basename='team')
router.register('photo', views.PhotoViewset, basename='photo')
router.register('categories', views.CategoryViewset, basename='categories')
router.register('level', views.LevelViewset, basename='level')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', index, name='accueil')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)