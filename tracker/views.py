from django.shortcuts import render
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Invoice

# Create your views here.
class InvoiceListView(ListView):
    template_name = "invoice_list.html"
    model = Invoice 

    @method_decorator(login_required(login_url='/login'))
    def dispatch(self, *args, **kwargs):
        return super(ListView, self).dispatch(*args, **kwargs)

    
