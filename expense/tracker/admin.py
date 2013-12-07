from django.contrib import admin
from .models import Store, Invoice, Item
# Register your models here.

class ItemInline(admin.TabularInline):
    model = Item
    fk_name = 'invoice'

class InvoiceAdmin(admin.ModelAdmin):

   list_display = ('store', 'total', 'date')
   list_filter = ('store', 'date')


   inlines = [
           ItemInline,
           ]


admin.site.register(Store)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Item)

