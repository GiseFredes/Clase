from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.indice, name="indice"),
    path('alumnos/listado',views.alumno_listado, name='alumnos_listado'),
    path('cursos/<int:inicio>', views.cursos, name="cursos"),
    path('alumnos/detalle/<str:nombreAlumno>', views.alumno_detalle, name='alumno_detalle'),
    re_path(r'alumnos/historico/(?P<year>[0-9]{4})/$', views.alumnos_historico, name='alumnos_historico'),
    path('alumnos/activos', views.alumnos_estado,{'estado':'activo'}, name="alumnos_activo"),
    path('alumnos/inactivos', views.alumnos_estado,{'estado':'inactivo'}, name="alumnos_inactivo"),

]
