from django.db import models
from django.db.models import Sum
from decimal import Decimal
import logging

logger = logging.getLogger(__name__)

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s' % self.name

class Invoice(models.Model):
    date = models.DateField()
    store = models.ForeignKey(Store, null=False)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __unicode__(self):
        return '%s at %s on %s' % (self.total, self.store.name, self.date)

    def calc_subtotal(self):
        return self.item_set.all().aggregate(Sum('item_total'))['item_total__sum']
   
    def calc_total(self):
        return self.subtotal * Decimal(1.14975)
    
    def save(self, **kwargs):
        self.subtotal = self.calc_subtotal()
        self.total = self.calc_total()
        super(Invoice,self).save()

class Item(models.Model):
    name = models.CharField(max_length=255)
    invoice = models.ForeignKey(Invoice,null=False)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=1)
    item_total = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def save(self, **kwargs):
        logger.info("Saving an item!")
        self.item_total = self.quantity * self.price
        super(Item,self).save()

    def __unicode__(self):
        return '%s x %s' % (self.quantity, self.name)
