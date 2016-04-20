from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^pending$', views.PaymentPendingView.as_view(), name='pending'),
]
