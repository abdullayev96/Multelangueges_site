from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('new/', CreateNew.as_view(), name = 'new'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('login/', Login, name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('contact/',contact, name='contact')
]