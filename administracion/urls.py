from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_administracion, name='index_administracion'),
    path('listadoEspecialidad/', views.ListEspecialidad.as_view(), name='listadoEspecialidad'),
    path('registroEspecialidad/', views.RegistroEspecialidadView.as_view(), name='registroEspecialidad'),
    path('editarEspecialidad/<int:pk>', views.ActualizarEspecialidadView.as_view(), name='editarEspecialidad'),
    path('eliminarEspecialidad/<int:pk>/', views.EliminarEspecialidadView.as_view(), name='eliminarEspecialidad'),
]