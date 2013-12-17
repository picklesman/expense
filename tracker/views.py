from django.shortcuts import render
from django.views.generic import ListView
from .models import Invoice

# Create your views here.
class InvoiceListView(ListView):
    template_name = "invoice_list.html"
    model = Invoice 

