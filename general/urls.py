from django.urls import path
from . import views

urlpatterns = [
    path('', views.app_homepage, name='home'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),
]
