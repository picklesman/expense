# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Invoice.total'
        db.alter_column(u'tracker_invoice', 'total', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2))

        # Changing field 'Invoice.subtotal'
        db.alter_column(u'tracker_invoice', 'subtotal', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2))

        # Changing field 'Item.price'
        db.alter_column(u'tracker_item', 'price', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2))

        # Changing field 'Item.item_total'
        db.alter_column(u'tracker_item', 'item_total', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2))

    def backwards(self, orm):

        # Changing field 'Invoice.total'
        db.alter_column(u'tracker_invoice', 'total', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2))

        # Changing field 'Invoice.subtotal'
        db.alter_column(u'tracker_invoice', 'subtotal', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2))

        # Changing field 'Item.price'
        db.alter_column(u'tracker_item', 'price', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2))

        # Changing field 'Item.item_total'
        db.alter_column(u'tracker_item', 'item_total', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2))

    models = {
        u'tracker.invoice': {
            'Meta': {'object_name': 'Invoice'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tracker.Store']"}),
            'subtotal': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '2'}),
            'total': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '2'})
        },
        u'tracker.item': {
            'Meta': {'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tracker.Invoice']"}),
            'item_total': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'})
        },
        u'tracker.store': {
            'Meta': {'object_name': 'Store'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['tracker']