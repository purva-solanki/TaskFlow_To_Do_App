from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='root'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('toggle_task/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]