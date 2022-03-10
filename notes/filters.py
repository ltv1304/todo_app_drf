from django_filters import rest_framework as filters
from notes.models import TODO, Project


class TODOFilter(filters.FilterSet):
    start_date = filters.IsoDateTimeFilter(field_name="published", lookup_expr='gte')
    end_date = filters.IsoDateTimeFilter(field_name="published", lookup_expr='lte')

    class Meta:
        model = TODO
        fields = ['project', 'start_date', 'end_date']


class ProjectFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['title']