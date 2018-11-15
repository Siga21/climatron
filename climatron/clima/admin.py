# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from clima.models import tipo_sensor, planta, modo, sensor, historico, calendario
from clima.models import estado, sensor_instalacion, historico_instalacion

class SensorAdmin(admin.ModelAdmin):
   list_display = ('nombre_sensor', 'tipo_sensor', 'planta', 'ip', 'ultima_temperatura', 'humedad', 'bateria', 'lectura', 'fecha_lectura')
   list_filter = ('planta','tipo_sensor')
   ordering = ('planta', 'tipo_sensor')

class HistoricoAdmin(admin.ModelAdmin):
   list_display = ('fecha', 'sensor', 'temperatura','humedad', 'bateria')
   list_filter = ('fecha','sensor')
   ordering = ('fecha', 'sensor')

class CalendarioAdmin(admin.ModelAdmin):
	list_display = ('fecha','sensor', 'modo')
	list_filter = ('fecha', 'sensor')
	ordering = ('fecha', 'sensor') 
	
class Sensor_InstalacionAdmin(admin.ModelAdmin):
	list_display = ('nombre_sensor', 'tipo_sensor', 'estado', 'valor', 'fecha_lectura')
	list_filter = ('nombre_sensor', 'tipo_sensor', 'estado')
	ordering = ('nombre_sensor', 'tipo_sensor')
		

admin.site.register(tipo_sensor)
admin.site.register(planta)
admin.site.register(modo)
admin.site.register(estado)
admin.site.register(sensor_instalacion, Sensor_InstalacionAdmin)
admin.site.register(historico_instalacion)
admin.site.register(sensor, SensorAdmin)
admin.site.register(historico, HistoricoAdmin)
admin.site.register(calendario, CalendarioAdmin)

