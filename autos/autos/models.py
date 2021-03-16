# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from six import python_2_unicode_compatible


@python_2_unicode_compatible
class Auto(models.Model):
    titulo = models.CharField(max_length=100, verbose_name=u'Título', unique=True)
    descripcion = models.TextField(help_text='Descripcion del AUTO')
    tipo_auto = models.ForeignKey(Tipo,on_delete=models.CASCADE)
    marca_auto = models.ForeignKey(Marca,on_delete=models.CASCADE)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

@python_2_unicode_compatible
class Marca(models.Model):
    Marca = models.CharField(max_length=100, verbose_name=u'Título', unique=True)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
@python_2_unicode_compatible
class Tipo(models.Model):
    Marca = models.CharField(max_length=100, verbose_name=u'Título', unique=True)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

@python_2_unicode_compatible
class Comentario(models.Model):
    auto = models.ForeignKey(Auto,on_delete=models.CASCADE)
    texto = models.TextField(help_text=u'Tú comentario', verbose_name='Comentario')

    def __str__(self):
        return self.texto
