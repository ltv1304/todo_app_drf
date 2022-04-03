from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import ServiceUser
from django.contrib.auth.models import Group


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)
        extra_kwargs = {
            'name': {
                'validators': [],
            }
        }


class UserSerializer(ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = ServiceUser
        fields = ('uid', 'username', 'email', 'first_name', 'last_name', 'groups',)


