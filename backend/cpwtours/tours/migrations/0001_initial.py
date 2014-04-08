# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TourRequest'
        db.create_table(u'tours_tourrequest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='R', max_length=1)),
            ('request_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('claim_time', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
        ))
        db.send_create_signal(u'tours', ['TourRequest'])


    def backwards(self, orm):
        # Deleting model 'TourRequest'
        db.delete_table(u'tours_tourrequest')


    models = {
        u'tours.tourrequest': {
            'Meta': {'object_name': 'TourRequest'},
            'claim_time': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'R'", 'max_length': '1'})
        }
    }

    complete_apps = ['tours']