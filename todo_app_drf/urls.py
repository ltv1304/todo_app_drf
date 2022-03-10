from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from notes.views import ProjectViewSet, TODOViewSet
from service_user.views import UserViewSet

user_router = DefaultRouter()
user_router.register('service_user', UserViewSet)

project_router = DefaultRouter()
project_router.register('project', ProjectViewSet)

todo_router = DefaultRouter()
todo_router.register('todo', TODOViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/users/', include(user_router.urls)),
    path('api/projects/', include(project_router.urls)),
    path('api/todos/', include(todo_router.urls)),
]
