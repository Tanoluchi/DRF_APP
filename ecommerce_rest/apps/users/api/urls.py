from django.urls import include, path

from .api import user_api_view

urlpatterns = [
    path('usuario/', user_api_view, name='user_api'),
]
