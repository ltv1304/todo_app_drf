from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from notes.filters import TODOFilter, ProjectFilter
from notes.models import Project, TODO
from notes.serializers import ProjectSerializer, TODOSerializer, TODOSerializerBase, ProjectSerializerBase


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_class = ProjectFilter
    pagination_class = ProjectLimitOffsetPagination

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ProjectSerializer
        return ProjectSerializerBase


class TODOLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class TODOViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer
    filterset_class = TODOFilter
    pagination_class = TODOLimitOffsetPagination

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(active_flag=False)

    def get_serializer_class(self):
        if self.request.method in ['GET', 'DELETE']:
            return TODOSerializer
        return TODOSerializerBase

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user, active_flag=True)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        instance_serializer = TODOSerializer(instance)
        return Response(instance_serializer.data)