from django.contrib import admin
from .models import Store, Invoice, Item
# Register your models here.

admin.site.register(Store)
admin.site.register(Invoice)
admin.site.register(Item)

