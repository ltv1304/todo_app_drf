from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from service_user.views import UserModelViewSet

router = DefaultRouter()
router.register('service_user', UserModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),

]
