from rest_framework.serializers import HyperlinkedModelSerializer
from .models import ServiceUser


class UserSerializer(HyperlinkedModelSerializer):
   class Meta:
       model = ServiceUser
       fields = '__all__' 
