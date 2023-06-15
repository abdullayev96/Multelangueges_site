from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name = 'home'),
    path('new/', CreateNew.as_view(), name = 'new'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),


    path('register/', SingUpView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name = 'login1.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        next_page='/'
    ), name='logout'),

    path('contact/',contact, name='contact')
]