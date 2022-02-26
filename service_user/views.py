from rest_framework.viewsets import ModelViewSet
from .models import ServiceUser 
from .serializers import UserModelSerializer 


class UserModelViewSet(ModelViewSet):
   queryset = ServiceUser.objects.all()
   serializer_class = UserModelSerializer
