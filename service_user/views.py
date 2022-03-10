from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .models import ServiceUser 
from .serializers import UserSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
   queryset = ServiceUser.objects.all()
   serializer_class = UserSerializer
