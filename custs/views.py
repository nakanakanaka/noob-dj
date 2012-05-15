from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from custs.models import Customer, CustomerForm, Suite, SuiteForm, Booking, BookingForm
# Create your views here.

"""no good
def customer_detail(request, customer_id):
    cust = get_object_or_404(Customer, pk=customer_id)
    form = CustomerForm(request.POST or None, instance=cust)
    
    return render_to_response('custs/customer_detail.html',
                              {' cust_form': form,
                               'cust_id': customer_id},
                               context_instance=RequestContext(request))
"""

"""def detail(request, cust_id):
    try:
        c = Customer.objects.get(pk=cust_id)
    except Customer.DoesNotExist:
        raise Http404
    return render_to_response("custs/customer_detail.html", {'customer': c})
"""
def customer_edit(request, customer_id):
    cust = get_object_or_404(Customer, pk=customer_id)
    form = CustomerForm(request.POST or None, instance=cust)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/custs/customers')
    return render_to_response('custs/customer_edit.html',
                              {'cust_form': form,
                               'cust_id': customer_id},
                              context_instance=RequestContext(request))

def customer_new(request):
    customer = Customer()
    form = CustomerForm(request.POST or None, instance=customer)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/custs/customers/')
    return render_to_response('custs/customer_new.html',
                              {'cust_form': form},
                              context_instance=RequestContext(request))

def suite_edit(request, suite_id):
    suite = get_object_or_404(Suite, pk=suite_id)
    form = SuiteForm(request.POST or None, instance=suite)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/custs/suites/')
    return render_to_response('custs/suite_edit.html',
                              {'suite_form': form,
                               'suite_id': suite_id},
                              context_instance=RequestContext(request))
def suite_new(request):
    form = SuiteForm(request.POST or None, instance=Suite())
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/custs/suites/')
    return render_to_response('custs/suite_new.html',
                              {'suite_form': form},
                              context_instance=RequestContext(request))
def booking_new(request):
    form = BookingForm(request.POST or None, instance=Booking())
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/custs/bookings/')
    return render_to_response('custs/booking_new.html',
                              {'booking_form': form},
                              context_instance=RequestContext(request))
def booking_edit(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    form = BookingForm(request.POST or None, instance=booking)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/custs/bookings/')
    return render_to_response('custs/booking_edit.html',
                              {'booking_form': form,
                               'booking_id': pk},
                              context_instance=RequestContext(request))
