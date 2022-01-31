from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
