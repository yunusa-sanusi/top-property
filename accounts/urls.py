from unicodedata import name
from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.signout, name='logout'),
]
