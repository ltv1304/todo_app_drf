import pytest

import requests
from rest_framework import status


class TestDeveloperPermissions:
    def test_can_view_todos(self, developer_headers):
        todo_view_response = requests.get('http://127.0.0.1:8000/api/todos/todo/', headers=developer_headers)
        assert todo_view_response.status_code == status.HTTP_200_OK

    def test_create_view_todos(self, developer_headers, user, project):
        content = 'Заметка'
        todo_create_response = requests.post('http://127.0.0.1:8000/api/todos/todo/',
                                           json={'project': project, 'content':content, 'user': user, 'active_flag': True},
                                           headers=developer_headers)
        assert todo_create_response.status_code == status.HTTP_201_CREATED

        todo = self.get_todo(developer_headers, content)
        todo_update_response = requests.put(f'http://127.0.0.1:8000/api/todos/todo/{todo}/',
                                             json={'project': project, 'content': 'Обновленная заметка', 'user': user,
                                                   'active_flag': True},
                                             headers=developer_headers)
        assert todo_update_response.status_code == status.HTTP_200_OK





    @staticmethod
    def get_todo(header, content):
        get_todo_list = requests.get('http://127.0.0.1:8000/api/todos/todo/',
                                      headers=header)
        todos_list = get_todo_list.json()['results']
        for todo in todos_list:
            if content == todo['content']:
                return todo['uid']