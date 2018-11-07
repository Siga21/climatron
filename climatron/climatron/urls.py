
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from clima import views
from clima.views import home
from clima.views import DetalleSensores_Instalacion

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^sensor_instalacion_detalle/(?P<pk>[0-9]+)/$', DetalleSensores_Instalacion.as_view(), name = 'sensores_instalacion'),
]

if settings.DEBUG:
     urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
