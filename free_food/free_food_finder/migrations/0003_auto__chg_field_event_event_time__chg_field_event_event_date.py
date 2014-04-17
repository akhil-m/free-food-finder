# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Event.event_time'
        db.alter_column(u'free_food_finder_event', 'event_time', self.gf('django.db.models.fields.TimeField')())

        # Changing field 'Event.event_date'
        db.alter_column(u'free_food_finder_event', 'event_date', self.gf('django.db.models.fields.DateField')())

    def backwards(self, orm):

        # Changing field 'Event.event_time'
        db.alter_column(u'free_food_finder_event', 'event_time', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Event.event_date'
        db.alter_column(u'free_food_finder_event', 'event_date', self.gf('django.db.models.fields.CharField')(max_length=30))

    models = {
        u'free_food_finder.event': {
            'Meta': {'object_name': 'Event'},
            'event_date': ('django.db.models.fields.DateField', [], {}),
            'event_description': ('django.db.models.fields.TextField', [], {}),
            'event_location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'event_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'event_time': ('django.db.models.fields.TimeField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['free_food_finder']