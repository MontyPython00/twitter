import pytest

from django.contrib.auth.models import User
from django.urls import reverse
from posts.models import Post, Comment, Like


pytestmark = pytest.mark.django_db

url_path = reverse('posts:create')

def test_create_post_success():
    user = User.objects.create_user(username='test', password='test')
    post_object = Post.objects.create(user=user,  description='test')
    assert Post.objects.all().count() == 1
    assert Post.objects.get(pk=1).user.username == user.username
    assert Post.objects.get(pk=1).description == post_object.description


def test_create_comment_success():
    user = User.objects.create_user(username='test', password='test')
    post_object = Post.objects.create(user=user, description='test')
    comment_object = Comment.objects.create(user=user, post=Post.objects.get(pk=1), text='Comment test.')
    assert Comment.objects.filter(post=Post.objects.get(pk=1)).count() == 1
    assert Comment.objects.filter(post=Post.objects.get(pk=1))[0].text == 'Comment test.'



def test_like_post_success():
    user = User.objects.create_user(username='test', password='test')
    user2 = User.objects.create_user(username='test2', password='test2')
    post_object = Post.objects.create(user=user, description='test')
    user_like_post = Like.objects.create(user=user, post=Post.objects.get(pk=1))
    user2_like_post = Like.objects.create(user=user2, post=Post.objects.get(pk=1))
    assert Like.objects.filter(post=post_object).count() == 2
    assert Like.objects.get(post=post_object, user=user).user.username == 'test'
    assert Like.objects.filter(post=post_object, user=user2).exists() == True
