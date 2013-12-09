from django.db import models
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

    def __unicode__(self):
        return '%s at %s on %s' % (self.total(), self.store.name, self.date)

    def total(self):

        all_invoices = self.item_set.all()

        total = 0
        for invoice in all_invoices:
            total += invoice.price * invoice.quantity

        return total

class Item(models.Model):
    name = models.CharField(max_length=255)
    invoice = models.ForeignKey(Invoice,null=False)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=1)
    item_total = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def save(self, **kwargs):
        logger.info("Saving an item!")
        self.item_total = self.quantity * self.price
        super(Item,self).save()

    def __unicode__(self):
        return '%s x %s' % (self.quantity, self.name)
