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
    assert response.status_code == 302
    assert User.objects.all().count() == 1
