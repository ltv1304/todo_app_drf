from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from service_user.models import ServiceUser
from service_user.views import UserViewSet

"""
    Test AuthorViewSet API with APIRequestFactory.
"""


class TestAuthorViewSet(TestCase):

    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.admin = ServiceUser.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.test_user = ServiceUser.objects.create(username='test',
                                                    email='test@mail.ru',
                                                    password='test123456'
                                                    )

    def test_access_denied_for_unauthorized_users(self):
        request = self.factory.get(f'')
        view = UserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authorized_users_have_access(self):
        request = self.factory.get(f'')
        force_authenticate(request, self.test_user)
        view = UserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_cant_delete_serviceuser(self):
        request = self.factory.delete(f'')
        force_authenticate(request, self.admin)
        view = UserViewSet.as_view({'delete': 'destroy'})
        with self.assertRaises(AttributeError):
            response = view(request, pk=self.test_user.uid)

    def test_users_cant_add_serviceuser(self):
        request = self.factory.post(f'')
        force_authenticate(request, self.admin)
        view = UserViewSet.as_view({'post': 'create'})
        with self.assertRaises(AttributeError):
            response = view(request)

    def test_users_can_retrieve_serviceuser(self):
        request = self.factory.get(f'')
        force_authenticate(request, self.admin)
        view = UserViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=self.test_user.uid)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_user_can_update_serviceuser(self):
        updated_name = 'Vasia'
        updated_email = 'vasia@mail.ru'
        request = self.factory.put(f'/api/users/service_user/{self.test_user.uid}/',
                                   {'username': updated_name, 'email': updated_email})
        force_authenticate(request, self.admin)
        view = UserViewSet.as_view({'put': 'update'})
        response = view(request, pk=self.test_user.uid)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        test = ServiceUser.objects.get(uid=self.test_user.uid)
        self.assertEqual(test.username, updated_name)
        self.assertEqual(test.email, updated_email)