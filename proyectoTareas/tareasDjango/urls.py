from django.urls import path
from . import views

app_name='tareasDjango'

urlpatterns=[
    path('',views.index,name='index'),
    path('consolaAdministrador',views.consolaAdministrador,name='consolaAdministrador'),
    path('cerrarSesion',views.cerrarSesion,name='cerrarSesion'),
    path('eliminarUsuario/<str:idUsuario>',views.eliminarUsuario,name='eliminarUsuario'),
    path('verUsuario/<str:idUsuario>',views.verUsuario,name='verUsuario'),
    path('nuevaTarea/<str:idUsuario>',views.nuevaTarea,name='nuevaTarea'),
    path('ejemploJavascript',views.ejemploJavascript,name='ejemploJavascript'),
    path('devolverMensaje',views.devolverMensaje,name='devolverMensaje'),
    path('conseguirInfoTarea',views.conseguirInfoTarea,name='conseguirInfoTarea'),
    path('publicarComentario',views.publicarComentario,name='publicarComentario'),
    path('reactDjango',views.reactDjango,name='reactDjango'),
    path('conseguirInfoUsuarios',views.conseguirInfoUsuarios,name='conseguirInfoUsuarios'),
    path('descargarReporteUsuarios',views.descargarReporteUsuarios,name='descargarReporteUsuarios')
    
]