from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import ServiceUser
from django.contrib.auth.models import Group


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class UserSerializer(HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True)

    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user

    def update(self, *args, **kwargs):
        user = super().update(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user

    class Meta:
        model = ServiceUser
        fields = fields = ('url', 'username', 'email', 'first_name', 'last_name', 'groups',)


