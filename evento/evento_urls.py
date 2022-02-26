from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista_registrados/', views.lista_personas, name='listado'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('registro/', views.registro_acceso_lista, name='registro_acceso_lista')
]
