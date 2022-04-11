import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType

from notes.models import Project, TODO
from service_user.models import ServiceUser


class UsersType(DjangoObjectType):
    class Meta:
        model = ServiceUser
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class TodoType(DjangoObjectType):
    class Meta:
        model = TODO
        fields = '__all__'

class Query(graphene.ObjectType):
    all_users = graphene.List(UsersType)
    all_projects = graphene.List(ProjectType)
    all_todos = graphene.List(TodoType)
    user_by_first_name = graphene.List(UsersType, name=graphene.String(required=True))

    def resolve_all_users(root, info):
        return ServiceUser.objects.all()

    def resolve_user_by_first_name(root, info, name):
        try:
            return ServiceUser.objects.filter(first_name__contains = name)
        except ServiceUser.DoesNotExist:
            return None

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_todos(root, info):
        return TODO.objects.all()


class TodoMutation(graphene.Mutation):
    class Arguments:
        content = graphene.String(required=True)
        uid = graphene.UUID()

    todo = graphene.Field(TodoType)

    @classmethod
    def mutate(cls, root, info, content, uid):
        todo = TODO.objects.get(pk=uid)
        todo.content = content
        todo.save()
        return TodoMutation(todo=todo)


class Mutation(graphene.ObjectType):
    update_todo = TodoMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)