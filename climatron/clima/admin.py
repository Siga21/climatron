# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from clima.models import tipo_sensor, planta, modo, sensor, historico, calendario

class SensorAdmin(admin.ModelAdmin):
   list_display = ('nombre_sensor', 'tipo_sensor', 'planta', 'ip', 'tb', 'tn', 'tc')
   list_filter = ('planta','tipo_sensor')
   ordering = ('planta', 'tipo_sensor')

class HistoricoAdmin(admin.ModelAdmin):
   list_display = ('fecha', 'sensor', 'temperatura')
   list_filter = ('fecha','sensor')
   ordering = ('fecha', 'sensor')

class CalendarioAdmin(admin.ModelAdmin):
	list_display = ('fecha','sensor', 'modo')
	list_filter = ('fecha', 'sensor')
	ordering = ('fecha', 'sensor') 

admin.site.register(tipo_sensor)
admin.site.register(planta)
admin.site.register(modo)
admin.site.register(sensor, SensorAdmin)
admin.site.register(historico, HistoricoAdmin)
admin.site.register(calendario, CalendarioAdmin)

