from django.urls import path, include
from . import views

urlpatterns = [
    path(r'', views.index, name='inicio'),
    path(r'inicio', views.index, name='inicio'),
    path(r'condiciones', views.condiciones, name='condiciones'),
]
