from rest_framework.viewsets import ModelViewSet
from .models import ServiseUser 
from .serializers import UserModelSerializer 


class UserModelViewSet(ModelViewSet):
   queryset = ServiseUser.objects.all()
   serializer_class = UserModelSerializer
