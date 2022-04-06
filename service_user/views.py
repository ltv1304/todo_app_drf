from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .models import ServiceUser 
from .serializers import UserSerializer, UserSerializerServiceInfo


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = ServiceUser.objects.all()

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return UserSerializerServiceInfo
        return UserSerializer

