from rest_framework.serializers import HyperlinkedModelSerializer
from .models import ServiseUser


class UserModelSerializer(HyperlinkedModelSerializer):
   class Meta:
       model = ServiseUser
       fields = '__all__'
