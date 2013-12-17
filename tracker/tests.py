from django.test import TestCase
from tracker.models import Item,Invoice,Store
from decimal import Decimal

# Create your tests here.
class ItemTestCase(TestCase):

    def setUp(self):
        self.store = Store.objects.create(name="Amazon")
        self.invoice = Invoice.objects.create(store=self.store,date="2013-12-11")


    def create_item(self, price, quantity):
        
        item = Item.objects.create(name="orange glasses", price=price, quantity=quantity, invoice=self.invoice)
        return item

    def test_total_is_correct(self):

        price = 20.00
        quantity = 4
        total = price * quantity

        item = self.create_item(price,quantity)

        self.assertEqual(item.item_total, total)
   
    def test_updating_item_updates_invoice(self):
        
        #create a line item, change the quantity and check that the invoice subtotal reflects this
        item = self.create_item(20,4)

        item.quantity -= 1
        item.save()

        self.assertEqual(item.invoice.subtotal, item.quantity * item.price)

    def test_deleting_item_updates_invoice(self):

        #create two line items, delete the first and check that the invoice subtotal equals the line item total
        item = self.create_item(20,5)
        second = self.create_item(10,4)

        invoice = item.invoice
    
        item.delete()

        self.assertEqual(invoice.subtotal, second.item_total)

    def test_invoice_total_is_correct(self):

        first = self.create_item(10,3)
        second = self.create_item(20, 1)

        subtotal = 10*3 + 20
        total = subtotal * 1.14975

        self.assertEqual(self.invoice.total.quantize(Decimal(0.00)), Decimal(total).quantize(Decimal(0.00)))
