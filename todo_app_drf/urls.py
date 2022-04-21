from django.contrib import admin
from django.urls import path, include, re_path
from graphene_django.views import GraphQLView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from notes.views import ProjectViewSet, TODOViewSet
from service_user.urls import router as beta_router

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

user_router = DefaultRouter()
v1_router = DefaultRouter()
v1_router.registry.extend(beta_router.registry)
v2_router = DefaultRouter()
v2_router.registry.extend(beta_router.registry)

project_router = DefaultRouter()
project_router.register('project', ProjectViewSet)

todo_router = DefaultRouter()
todo_router.register('todo', TODOViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Todo App",
        default_version='0.5',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/users/v1/', include((v1_router.urls, 'api'), namespace='v1')),
    path('api/users/v2/', include((v2_router.urls, 'api'), namespace='v2')),
    path('api/projects/', include(project_router.urls)),
    path('api/todos/', include(todo_router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
]
