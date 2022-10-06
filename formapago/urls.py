from django.urls import path
from . import views

urlpatterns = [
    path(r'formapago/', views.index, name='formapago'),
 #   path(r'^micuenta/$', views.mi_cuenta,name='mi_cuenta'),
 #   path(r'^misdatos/$', views.mis_datos, name='mis_datos'), #URL Valida
  
]
