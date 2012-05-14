from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from custs.models import Customer
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^custs/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Customer,
            template_name='custs/customer_detail.html')),
    url(r'^custs/customer_edit/(?P<customer_id>\d+)/$', 
        'custs.views.customer_edit')
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #url(r'^custs/$', 'custs.views.index'),
    #url(r'^custs/(?P<cust_id>\d+)/$', 'custs.views.detail'),
)
