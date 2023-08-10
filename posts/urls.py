from django.urls import path
from posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.home_view, name='home_page'),
    path('<int:id>/', views.post_view, name='post'),
    path('create/', views.create_view, name='create'),
    path('profile/<str:username>', views.profile_view, name='profile')
]