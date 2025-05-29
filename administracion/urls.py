from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_administracion, name='index_administracion'),

    path('listadoEspecialidad/', views.ListEspecialidad.as_view(), name='listadoEspecialidad'),
    path('registroEspecialidad/', views.RegistroEspecialidadView.as_view(), name='registroEspecialidad'),
    path('editarEspecialidad/<int:pk>', views.ActualizarEspecialidadView.as_view(), name='editarEspecialidad'),
    path('eliminarEspecialidad/<int:pk>/', views.EliminarEspecialidadView.as_view(), name='eliminarEspecialidad'),

    path('listadoOcupacion/', views.ListOcupacion.as_view(), name='listadoOcupacion'),
    path('registroOcupacion/', views.RegistroOcupacionView.as_view(), name='registroOcupacion'),
    path('editarOcupacion/<int:pk>', views.ActualizarOcupacionView.as_view(), name='editarOcupacion'),
    path('eliminarOcupacion/<int:pk>/', views.EliminarOcupacionView.as_view(), name='eliminarOcupacion'),

    path('listadoProfesional/', views.ListProfesional.as_view(), name='listadoProfesional'),
    path('crearProfesional/', views.CrearProfesionalView.as_view(), name='crearProfesional'),

]