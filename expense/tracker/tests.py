from django.test import TestCase
from tracker.models import Item,Invoice,Store

# Create your tests here.
class ItemTestCase(TestCase):

    def setUp(self):
        self.store = Store.objects.create(name="Amazon")
        self.invoice = Invoice.objects.create(store=self.store,date="2013-12-11")

    def test_total_is_correct(self):

        price = 20.00
        quantity = 4
        total = price * quantity

        item = Item.objects.create(name="orange glasses", 
                                   price=price,
                                   quantity=quantity,
                                   invoice=self.invoice)

        self.assertEqual(item.item_total, total)
