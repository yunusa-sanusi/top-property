from unicodedata import name
from django.urls import path
from . import views

app_name = 'properties'
urlpatterns = [
    path('', views.property_list_view, name='property-list'),
    path('create/', views.property_create_view, name='property-create'),
    path('<slug:slug>/', views.property_detail_view, name='property-detail'),
    path('<slug:slug>/update/', views.property_update_view, name='property-update'),
    path('<slug:slug>/delete/', views.property_delete_view, name='property-delete'),
]
