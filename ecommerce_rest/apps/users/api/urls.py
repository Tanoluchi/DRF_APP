from django.urls import include, path

from .api import UserApiView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'usuario', UserApiView, basename='usuario')

urlpatterns = [
    path(r'', include(router.urls)),
]
