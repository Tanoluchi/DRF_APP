from rest_framework import viewsets
from rest_framework.response import Response

from apps.users.models import User

from .serializers import UserSerializer

from rest_framework.decorators import action


class UserApiView(viewsets.GenericViewSet):
    
    lookup_field = 'id'
    
    @action(methods=('get', ), detail=True)
    def detalle(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs.get(self.lookup_field))
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)