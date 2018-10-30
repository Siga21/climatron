# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime, timedelta
from django.utils import timezone

from clima.models import sensor, sensor_instalacion 

# Create your views here.
def home(request):

	sensores = sensor.objects.order_by('planta')
	instalacion = sensor_instalacion.objects.order_by('tipo_sensor')
	context = {'los_sensores': sensores , 'las_instalaciones' : instalacion}
	return render(request, 'clima/home.html', context)