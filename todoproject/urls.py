from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),  # Include all todo app URLs
    path('accounts/', include('django.contrib.auth.urls')),  # For built-in auth
]