# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Comment'
        db.delete_table(u'free_food_finder_comment')

        # Removing M2M table for field user on 'Comment'
        db.delete_table(db.shorten_name(u'free_food_finder_comment_user'))


    def backwards(self, orm):
        # Adding model 'Comment'
        db.create_table(u'free_food_finder_comment', (
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['free_food_finder.Event'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'free_food_finder', ['Comment'])

        # Adding M2M table for field user on 'Comment'
        m2m_table_name = db.shorten_name(u'free_food_finder_comment_user')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comment', models.ForeignKey(orm[u'free_food_finder.comment'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['comment_id', 'user_id'])


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