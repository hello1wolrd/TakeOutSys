"""TakeOutSys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

from config import settings
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="sort/sortshow.html")),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^profile/', include('personinfo.urls', namespace='profile')),
    url(r'^product/', include('product.urls', namespace='product')),
    url(r'^verify/', include('verify.urls', namespace='verify')),
    url(r'^payment/', include('payment.urls', namespace='payment')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


