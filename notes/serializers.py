from rest_framework.relations import StringRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from notes.models import Project, TODO


class ProjectSerializerBase(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class TODOSerializerBase(ModelSerializer):
    class Meta:
        model = TODO
        # fields = '__all__'
        fields = ['content', 'project']


class TODOSerializer(ModelSerializer):
    class Meta:
        model = TODO
        fields = '__all__'