from rest_framework.viewsets import ModelViewSet

from notes.models import Project, TODO
from notes.serializers import ProjectSerializer, TODOSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TODOViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer