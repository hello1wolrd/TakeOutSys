from django.conf.urls import url

from . import views

urlpatterns = [ 
    url(r'^(?P<pk>.*)/$', views.VerifyView.as_view(), name='verify'),
]
