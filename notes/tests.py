import json

from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from requests.auth import HTTPBasicAuth
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from mixer.backend.django import mixer

from notes.models import Project, TODO
from service_user.models import ServiceUser
from rest_framework.test import RequestsClient

"""
    Test ProjectViewSet API with APIRequestFactory.
"""


class TestProjectViewSet(TestCase):
    def setUp(self) -> None:
        self.admin = ServiceUser.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.test_user = ServiceUser.objects.create(username='test',
                                                email='test@mail.ru',
                                                password='test123456'
                                                )
        self.client = APIClient()
        self.project = mixer.blend(Project)

    def test_access_denied_for_unauthorized_users(self):
        response = self.client.get(f'/api/projects/project/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authorized_users_have_access(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(f'/api/projects/project/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

    def test_users_can_delete_projects(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.delete(f'/api/projects/project/{self.project.uid}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_users_cant_add_projects(self):
        self.client.force_authenticate(user=self.admin)
        user = ServiceUser.objects.first()
        response = self.client.post(f'/api/projects/project/',
                                    {'title':'new_project', 'path': 'path', 'users': [user.uid]})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_users_can_retrieve_projects(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(f'/api/projects/project/{self.project.uid}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_user_can_update_projects(self):
        updated_path = '42'
        updated_title = 'project_42'
        user = ServiceUser.objects.first()
        self.client.force_authenticate(user=self.admin)
        test = Project.objects.get(uid=self.project.uid)
        self.assertNotEqual(test.path, updated_path)
        self.assertNotEqual(test.title, updated_title)
        response = self.client.put(f'/api/projects/project/{self.project.uid}/',
                                   {'path': updated_path, 'title': updated_title, 'users': [user.uid]})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        test = Project.objects.get(uid=self.project.uid)
        self.assertEqual(test.path, updated_path)
        self.assertEqual(test.title, updated_title)


"""
    Test TODOViewSet API with APIRequestFactory.
"""


class TestTodoViewSet(APITestCase):
    def setUp(self) -> None:
        self.admin = ServiceUser.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.test_user = ServiceUser.objects.create(username='test',
                                                email='test@mail.ru',
                                                password='test123456'
                                                )
        self.todo = mixer.blend(TODO)

    def test_access_denied_for_unauthorized_users(self):
        response = self.client.get('/api/todos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authorized_users_have_access(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(f'/api/todos/todo/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

    def test_users_can_delete_todos(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.delete(f'/api/todos/todo/{self.todo.uid}/')
        todo = TODO.objects.first()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(todo.active_flag)

    def test_users_cant_add_todos(self):
        self.client.force_authenticate(user=self.admin)
        user = ServiceUser.objects.first()
        project = Project.objects.first()
        response = self.client.post(f'/api/todos/todo/',
                                    {'project': project.uid, 'content':'42', 'users': user.uid, 'active_flag': True})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_users_can_retrieve_todos(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(f'/api/todos/todo/{self.todo.uid}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_user_can_update_todos(self):
        updated_content = '42'
        test_user_2 = ServiceUser.objects.create(username='test_2',
                                                  email='test_2@mail.ru',
                                                  password='test123456'
                                                 )
        project = Project.objects.first()
        self.client.force_authenticate(user=self.admin)
        test = TODO.objects.get(uid=self.todo.uid)
        self.assertNotEqual(test.content, updated_content)
        self.assertNotEqual(test.user, test_user_2.uid)
        response = self.client.put(f'/api/todos/todo/{self.todo.uid}/',
                                   {'project': project.uid, 'content': updated_content, 'user': test_user_2.uid, 'active_flag': True})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        test = TODO.objects.get(uid=self.todo.uid)
        self.assertEqual(test.content, updated_content)
        self.assertEqual(test.user.uid, test_user_2.uid)


class TestGroupPermissions(APITestCase):
    def test_api_client(self):
        client = RequestsClient()
        self.admin = ServiceUser.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        response = client.post('http://127.0.0.1:8000/api-token-auth/', json={"username": "admin", "password": "admin123456"})
        print(response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_200_OK)