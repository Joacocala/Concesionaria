from django.urls import path
from Gestion import views

urlpatterns = [path("", views.Inicio, name="inicio"),
              path("formulariocliente",views.formulario_cliente,name="formulariocliente"),
              path("formulario_empleado",views.formulario_empleado,name="formulario_empleado"),
              path("formulario_vehiculo",views.formulario_vehiculo,name="formulario_vehiculo"),
              path("busqueda_empleado",views.busqueda_empleado,name="busqueda_empleado"),
              


              

 ]

