from django.conf.urls import url

from . import views

urlpatterns = [ 
    url(r'^add/$', views.ProductAddView.as_view(), name='addproduct'),
    url(r'^(?P<pk>\d+)/change/$', views.ProductChangeView.as_view(), name='changeproduct'),
    url(r'^books/page/(?P<page>\d{1,2})$', views.ProductBooksView.as_view(), name='books'),
    url(r'^computers/page/(?P<page>\d{1,2})$', views.ProductComputersView.as_view(), name='computers'),
    url(r'^video/page/(?P<page>\d{1,2})$', views.ProductVideoView.as_view(), name='video'),
    url(r'^dress/page/(?P<page>\d{1,2})$', views.ProductDressView.as_view(), name='dress'),
    url(r'^grocery/page/(?P<page>\d{1,2})$', views.ProductGroceryView.as_view(), name='grocery'),
    url(r'^top/books$', views.ProductTopBooksView.as_view(), name='topbooks'),

]
