
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from clima import views
from clima.views import home
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
]

if settings.DEBUG:
     urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
