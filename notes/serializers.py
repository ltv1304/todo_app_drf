from rest_framework.relations import HyperlinkedRelatedField, StringRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from notes.models import Project, TODO
from service_user.models import ServiceUser


class ProjectSerializer(ModelSerializer):
    # users = HyperlinkedRelatedField(view_name='serviceuser-detail',
    #                                 queryset=ServiceUser.objects.all(),
    #                                 many=True)

    users = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class TODOSerializer(ModelSerializer):
    # project = HyperlinkedRelatedField(view_name='project-detail',
    #                                   queryset=Project.objects.all())
    # user = HyperlinkedRelatedField(view_name='serviceuser-detail',
    #                                queryset=ServiceUser.objects.all())

    user = StringRelatedField()
    project = StringRelatedField()

    class Meta:
        model = TODO
        fields = '__all__'