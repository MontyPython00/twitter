import pytest

from django.contrib.auth.models import User
from django.urls import reverse
from accounts.forms import LoginForm, RegisterForm

pytestmark = pytest.mark.django_db


#Integration Tests 


def test_create_account_client_success(client):
    client_url = reverse('accounts:signup')
    response = client.post(path=client_url, data={
        "username":"test123123",
        "email": "test@domain.pl",
        "password1": "myPassword123",
        "password2": "myPassword123"
    })
    assert response.status_code == 302 #code 302 moves to another location in that case is home page - valid data
    assert User.objects.all().count() == 1
    assert User.objects.get(pk=1).username == 'test123123'

def test_create_account_client_failed(client):
    client_url = reverse('accounts:signup')
    response = client.post(path=client_url, data={
        "username":"test123123",
        "email": "test@domain.pl",
        "password1": "myPassword",
        "password2": "myPassword"
    })
    assert response.status_code == 200 # code 200, the request was successful but data are wrong


def test_sign_in_client_success(client):
    user = User.objects.create_user(username='test', password='test123')
    client_url = reverse('accounts:login')
    response = client.post(path=client_url, data={
        "username": 'test',
        "password": 'test123'
    })
    assert response.status_code == 302 #code 302 moves to another location in that case is home page - valid data


def test_sign_in_client_failed(client):
    user = User.objects.create_user(username='test', password='test123')
    client_url = reverse('accounts:login')
    response = client.post(path=client_url, data={
        "username": 'test',
        "password": 'test1231'
    })
    assert response.status_code == 200 # code 200, the request was successful but data are wrong
