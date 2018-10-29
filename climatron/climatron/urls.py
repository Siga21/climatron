
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from clima import views
from clima.views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
]
