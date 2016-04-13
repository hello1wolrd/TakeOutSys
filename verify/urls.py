from django.conf.urls import url

from . import views

urlpatterns = [ 
    url(r'^verify/(?P<pk>\w+)$', views.VerifyView.as_view(), name='verify'),
]
