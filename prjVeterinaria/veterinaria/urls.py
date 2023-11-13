from django.urls import path
from . import views


urlpatterns = [
   path('/', views.acerca_de, name='acerca_de'),
   path('clientes', views.clientes, name='clientes'),
   path('detalle_cliente/<int:pk>', views.detalle_cliente, name='detalle_cliente'),
   path('nuevo_cliente', views.nuevo_cliente, name='nuevo_cliente'),
   path('modificar_cliente/<int:pk>', views.modificar_cliente, name='modificar_cliente'),
   path('eliminar_cliente/<int:pk>', views.eliminar_cliente, name='eliminar_cliente'),
   path('localidades', views.localidades, name='localidades'),
   path('nueva_localidad', views.nueva_localidad, name='nueva_localidad'),
   path('modificar_localidad/<int:pk>', views.modificar_localidad, name='modificar_localidad'),
   path('eliminar_localidad/<int:pk>', views.eliminar_localidad, name='eliminar_localidad'),
   path('tipo_doc', views.tipo_doc, name='tipo_doc'),
   path('nuevo_pais', views.nuevo_pais, name='nuevo_pais'),
   path('provincias', views.provincias, name='provincias'),
   path('nueva_provincia', views.nueva_provincia, name='nueva_provincia'),
   path('modificar_provincia/<int:pk>', views.modificar_provincia, name='modificar_provincia'),
   path('eliminar_provincia/<int:pk>', views.eliminar_provincia, name='eliminar_provincia'),
   path('nueva_mascota', views.nueva_mascota, name='nueva_mascota'),

]