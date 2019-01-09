from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.UserView, name='users'),
    path('groups', views.GroupView, name='groups'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
