# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'free_food_finder_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('event_time', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('event_date', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('event_description', self.gf('django.db.models.fields.TextField')()),
            ('event_location', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'free_food_finder', ['Event'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'free_food_finder_event')


    models = {
        u'free_food_finder.event': {
            'Meta': {'object_name': 'Event'},
            'event_date': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'event_description': ('django.db.models.fields.TextField', [], {}),
            'event_location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'event_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'event_time': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['free_food_finder']