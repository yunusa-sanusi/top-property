from django.urls import path
from . import views

app_name = 'agents'
urlpatterns = [
    path('', views.agent_list_view, name='agent-list'),
    path('<slug:slug>/', views.agent_details_view, name='agent-detail'),
    path('<slug:slug>/edit/', views.agent_edit_view, name='agent-edit'),
]
