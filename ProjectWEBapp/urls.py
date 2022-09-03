from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inicio, name='Inicio'),
    path('nosotros', views.Nosotros, name='Nosotros'),
    path('Usuarios', views.Usuarios, name='Usuarios'),
    path('Usuarios/crear', views.crear_usuario, name='crear'),
    path('Usuarios/actualizar', views.actualizar_usuario, name='actualizar'),
    path('Departamentos', views.Departamentos, name='Departamentos'),
    path('Departamentos/creardep', views.crear_departamento, name='creardep'),
    path('Departamentos/actualizardep', views.actualizar_departamento, name='actualizardep'),
]