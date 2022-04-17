import pytest
import requests


@pytest.fixture()
def admin_headers():
    response = requests.post('http://127.0.0.1:8000/api-token-auth/',
                             json={"username": "test_2", "password": "test_2"})
    headers = {'Authorization': f'Token {response.json()["token"]}'}
    return headers


@pytest.fixture()
def project_manager_headers():
    response = requests.post('http://127.0.0.1:8000/api-token-auth/',
                             json={"username": "test_1", "password": "test_1"})
    headers = {'Authorization': f'Token {response.json()["token"]}'}
    return headers


@pytest.fixture()
def developer_headers():
    response = requests.post('http://127.0.0.1:8000/api-token-auth/',
                             json={"username": "test_0", "password": "test_0"})
    headers = {'Authorization': f'Token {response.json()["token"]}'}
    return headers


@pytest.fixture()
def user(developer_headers):
    get_users_list = requests.get('http://127.0.0.1:8000/api/users/service_user/',
                                  headers=developer_headers)
    users_list = get_users_list.json()['results']
    for user in users_list:
        if 'test_0' == user['username']:
            return user['uid']


@pytest.fixture()
def project(developer_headers):
    get_projects_list = requests.get('http://127.0.0.1:8000/api/projects/project/',
                                     headers=developer_headers)
    project_uid = get_projects_list.json()['results'][0]['uid']
    return project_uid

@pytest.fixture()
def todo_content(request, developer_headers):
    content = 'Заметка'

    return content