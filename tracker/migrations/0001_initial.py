# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Store'
        db.create_table(u'tracker_store', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'tracker', ['Store'])

        # Adding model 'Invoice'
        db.create_table(u'tracker_invoice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('store', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tracker.Store'])),
        ))
        db.send_create_signal(u'tracker', ['Invoice'])

        # Adding model 'Item'
        db.create_table(u'tracker_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('invoice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tracker.Invoice'])),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('quantity', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
        ))
        db.send_create_signal(u'tracker', ['Item'])


    def backwards(self, orm):
        # Deleting model 'Store'
        db.delete_table(u'tracker_store')

        # Deleting model 'Invoice'
        db.delete_table(u'tracker_invoice')

        # Deleting model 'Item'
        db.delete_table(u'tracker_item')


    models = {
        u'tracker.invoice': {
            'Meta': {'object_name': 'Invoice'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tracker.Store']"})
        },
        u'tracker.item': {
            'Meta': {'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tracker.Invoice']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'})
        },
        u'tracker.store': {
            'Meta': {'object_name': 'Store'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['tracker']