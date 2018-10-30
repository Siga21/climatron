# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse

# Modelos.
# tipos de sensor -------------------------------------------------
class tipo_sensor(models.Model):
	nombre_tipo_sensor = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural = "Tipos_Sensores"

	def __unicode__(self):
		return self.nombre_tipo_sensor

# plantas ---------------------------------------------------------
class planta(models.Model):
	nombre_planta = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural = "Plantas"

	def __unicode__(self):
		return self.nombre_planta

# modos -----------------------------------------------------------
class modo(models.Model):
	nombre_modo = models.CharField(max_length=100)
	
	class Meta:
		verbose_name_plural = "Modos"

	def __unicode__(self):
		return self.nombre_modo
 
# sensores --------------------------------------------------------
class sensor(models.Model):
	nombre_sensor = models.CharField(max_length=100)
	tipo_sensor = models.ForeignKey(tipo_sensor, default=None, null=False, blank=False)
	planta = models.ForeignKey(planta, default=None, null=False, blank=False)
	ip = models.CharField(max_length=200)
	tb = models.DecimalField(max_digits=5, decimal_places=2)
	tn = models.DecimalField(max_digits=5, decimal_places=2)
	tc = models.DecimalField(max_digits=5, decimal_places=2)
	ultima_temperatura = models.DecimalField(max_digits=5, decimal_places=2, default=0)

	class Meta:
		verbose_name_plural = "Sensores"

	def __unicode__(self):
		return self.nombre_sensor

# historico --------------------------------------------------------
class historico(models.Model):
	fecha = models.DateTimeField(default=datetime.now, blank=True)
	sensor = models.ForeignKey(sensor, default=None, null=False, blank=False)
	temperatura = models.DecimalField(max_digits=5, decimal_places=2)

	class Meta:
		verbose_name_plural = "Historico"

	def __unicode__(self):
		return self.sensor.nombre_sensor  

# calendario -------------------------------------------------------
class calendario(models.Model):
	fecha = models.DateTimeField(default=datetime.now, blank= False)
	sensor = models.ForeignKey(sensor, default=None, null=False, blank=False)
	modo = models.ForeignKey(modo, default=None, null=False, blank=False)

	class Meta:
		verbose_name_plural = "Calendario"

	def __unicode__(self):
		return self.sensor.nombre_sensor 

 
# estado ----------------------------------------------------------
class estado(models.Model):
	codigo = models.IntegerField(default=0)
	nombre_estado = models.CharField(max_length=100)
	
	class Meta:
		verbose_name_plural = "Estados"

	def __unicode__(self):
		return self.nombre_estado

# sensores instalacion   ------------------------------------------
class sensor_instalacion(models.Model):
	nombre_sensor = models.CharField(max_length=100)
	tipo_sensor = models.ForeignKey(tipo_sensor, default=None, null=False, blank=False)
	estado = models.ForeignKey(estado, default=None, null=False, blank=False)

	class Meta:
		verbose_name_plural = "Sensores instalación"

	def __unicode__(self):
		return self.nombre_sensor
	