from django.contrib import admin
from .models import Store, Invoice, Item
# Register your models here.

class ItemInline(admin.TabularInline):
    model = Item
    fk_name = 'invoice'
    readonly_fields = ('item_total',)

class InvoiceAdmin(admin.ModelAdmin):

   list_display = ('store', 'total', 'date')
   list_filter = ('store', 'date')
   readonly_fields = ('subtotal', 'total')

   inlines = [
           ItemInline,
           ]

class ItemAdmin(admin.ModelAdmin):
    readonly_fields = ('item_total',)

admin.site.register(Store)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Item, ItemAdmin)

