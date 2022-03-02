from rest_framework.serializers import HyperlinkedModelSerializer
from .models import ServiceUser


class UserModelSerializer(HyperlinkedModelSerializer):
   class Meta:
       model = ServiceUser
       fields = '__all__' 
