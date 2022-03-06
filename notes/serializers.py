from rest_framework.relations import HyperlinkedRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer

from notes.models import Project, TODO
from service_user.models import ServiceUser


class ProjectSerializer(HyperlinkedModelSerializer):
    users = HyperlinkedRelatedField(view_name='serviceuser-detail',
                                    queryset=ServiceUser.objects.all(),
                                    many=True)

    class Meta:
        model = Project
        fields = '__all__'


class TODOSerializer(HyperlinkedModelSerializer):
    project = HyperlinkedRelatedField(view_name='project-detail',
                                      queryset=Project.objects.all())
    user = HyperlinkedRelatedField(view_name='serviceuser-detail',
                                   queryset=ServiceUser.objects.all())

    class Meta:
        model = TODO
        fields = '__all__'