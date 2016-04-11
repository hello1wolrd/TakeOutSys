from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^config/$', views.PersonConfigView.as_view(), name='config'),
    url(r'^detail/$', views.PersonConfigView.as_view(), name='detail'),
]
