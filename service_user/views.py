from rest_framework.viewsets import ModelViewSet
from .models import ServiceUser 
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
   queryset = ServiceUser.objects.all()
   serializer_class = UserSerializer
