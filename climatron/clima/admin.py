# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from clima.models import tipo_sensor, planta, modo, sensor, historico, calendario

admin.site.register(tipo_sensor)
admin.site.register(planta)
admin.site.register(modo)
admin.site.register(sensor)
admin.site.register(historico)
admin.site.register(calendario)

