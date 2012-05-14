from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from custs.models import Customer, CustomerForm
# Create your views here.

def detail(request, cust_id):
    try:
        c = Customer.objects.get(pk=cust_id)
    except Customer.DoesNotExist:
        raise Http404
    return render_to_response("custs/customer_detail.html", {'customer': c})

def customer_edit(request, customer_id):
    cust = get_object_or_404(Customer, pk=customer_id)
    form = CustomerForm(request.POST or None, instance=cust)
    
    if form.is_valid():
        form.save()
        return HttpResponse("Success!")
    return render_to_response('custs/customer_edit.html',
                              {'cust_form': form,
                               'cust_id': customer_id},
                              context_instance=RequestContext(request))