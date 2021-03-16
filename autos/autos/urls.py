from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.inicio, name='inicio'),
    url(r'^cerrar/$', views.cerrar, name='cerrar'),
    url(r'^comenta/$', views.comentario_nuevo, name='comentario_nuevo'),
    url(r'^contacto/$', views.contacto, name='contacto'),
    url(r'^ingresar/$', views.ingresar, name='ingresar'),
    url(r'^autos/$', views.autos, name='lista_autos'),
    url(r'^auto/nuevo/$', views.auto_nuevo, name='auto_nuevo'),
    url(r'^auto/(?P<id_auto>\d+)$', views.auto, name='detalle_auto'),
    url(r'^usuarios/$', views.usuarios, name='usuarios'),
    url(r'^usuario/nuevo/$', views.usuario_nuevo, name='usuario_nuevo'),
    url(r'^sobre/$', views.sobre, name='sobre'),
]
