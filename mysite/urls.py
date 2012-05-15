from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from custs.models import Customer, Suite, Booking
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^custs/customers/$',
        ListView.as_view(queryset=Customer.objects.all(),)),
    
    url(r'^custs/customer_detail/(?P<pk>\d+)/$',
        DetailView.as_view(
                           model=Customer,)),
                           #template_name='custs/customer_detail.html')),
    url(r'^custs/customer_edit/(?P<customer_id>\d+)/$', 
        'custs.views.customer_edit'),
    url(r'^custs/customer_new/$', 'custs.views.customer_new'),
    url(r'^custs/suites/$', ListView.as_view(queryset=Suite.objects.all())),
    #url(r'^custs/suite_detail/(?P<pk>\d+)/$',
    #    DetailView.as_view(model=Suite)),
    url(r'^custs/suite_edit/(?P<suite_id>\d+)/$', 
        'custs.views.suite_edit'),
    url(r'^custs/suite_new/$', 'custs.views.suite_new'),
    url(r'^custs/bookings/$', ListView.as_view(queryset=Booking.objects.all())),
    #url(r'^custs/booking_detail/(?P<pk>\d+)/$',
    #    DetailView.as_view(model=Booking)),
    url(r'^custs/booking_edit/(?P<pk>\d+)/$', 'custs.views.booking_edit'),
    url(r'^custs/booking_new/$', 'custs.views.booking_new'),
)